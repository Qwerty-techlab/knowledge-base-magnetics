# -*- coding: utf-8 -*-
"""Чертежи для отчёта по дросселю фазы многофазного interleaved boost.

Формирует PNG в 1_output_files/img_3ph/ по данным
5_interleaved/results_interleaved.json. Стилистика повторяет
3_calc/make_drawings.py (тот же шрифт, оформление выносок и подписей).

Состав:
    winding_<f>.png    — осевое сечение с ЕДИНЫМ зазором и укладкой витков;
    phases_<f>.png     — токи фаз с равномерным сдвигом и суммарный входной;
    waveform_<f>.png   — напряжение на дросселе и ток фазы за период;
    ripple_vs_D.png    — коэффициент подавления пульсаций K(D) при N = 1…4;
    impedance.png      — |Z(f)| с отметкой собственного резонанса.
"""
import json
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
IMG_DIR = os.path.join(ROOT, "1_output_files", "img_3ph")
os.makedirs(IMG_DIR, exist_ok=True)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import interleaved_design as il

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10,
    "axes.grid": False,
})

def winding_layout(selected, f_lbl, path):
    """Фронтальное сечение комплекта сердечника с реальной укладкой кабелей."""
    core = selected["core"]
    design = selected["design"]
    wire = selected["wire"]
    layout = design["winding_layout"]
    outer = core["outer_width_mm"]
    set_height = core["set_height_mm"]
    center = core["d_center_mm"]
    inside = core["d_bore_mm"]
    window_h = core["h_window_mm"]
    outer_leg = (outer - inside) / 2.0
    x_center = center / 2.0
    x_outer_inner = inside / 2.0
    y_window = window_h / 2.0
    y_outer = set_height / 2.0
    gap = design["gap_mm"]

    fig, ax = plt.subplots(figsize=(8.0, 6.4))
    ferrite = dict(facecolor="0.78", edgecolor="black", hatch="//", lw=0.8)
    ax.add_patch(Rectangle((-outer / 2.0, y_window), outer,
                           y_outer - y_window, **ferrite))
    ax.add_patch(Rectangle((-outer / 2.0, -y_outer), outer,
                           y_outer - y_window, **ferrite))
    ax.add_patch(Rectangle((-outer / 2.0, -y_window), outer_leg,
                           2.0 * y_window, **ferrite))
    ax.add_patch(Rectangle((x_outer_inner, -y_window), outer_leg,
                           2.0 * y_window, **ferrite))
    ax.add_patch(Rectangle((-x_center, gap / 2.0), center,
                           y_window - gap / 2.0, **ferrite))
    ax.add_patch(Rectangle((-x_center, -y_window), center,
                           y_window - gap / 2.0, **ferrite))
    ax.add_patch(Rectangle((-x_center, -gap / 2.0), center, gap,
                           facecolor="white", edgecolor="black", lw=0.8))

    d = wire["d_outer_mm"]
    spacing = layout["turn_spacing_mm"]
    n_axial = int(layout["parallel_axial"])
    n_radial = int(layout["parallel_radial"])
    turns_bank = int(layout["turns_per_bank_per_layer"])
    n_layers = int(layout["n_layers"])
    keepout = layout["gap_keepout_half_mm"]
    radial_step = layout["group_radial_mm"] + layout["interlayer_insulation_mm"]
    turn_pitch = layout["turn_pitch_mm"]
    remaining = int(design["N"])

    for layer in range(n_layers):
        for bank_sign in (1, -1):
            for turn_index in range(turns_bank):
                if remaining <= 0:
                    break
                group_bottom = keepout + turn_index * turn_pitch
                for ia in range(n_axial):
                    y_abs = group_bottom + d / 2.0 + ia * (d + spacing)
                    y = bank_sign * y_abs
                    for ir in range(n_radial):
                        cable_index = ir * n_axial + ia
                        if cable_index >= wire["n_parallel"]:
                            continue
                        x = x_center + 0.75 + layer * radial_step + d / 2.0 + ir * (d + spacing)
                        for sign_x in (-1, 1):
                            ax.add_patch(Circle((sign_x * x, y), 0.46 * d,
                                                facecolor="#c77720", edgecolor="black",
                                                lw=0.25))
                remaining -= 1

    for y in (-keepout, keepout):
        ax.axhline(y, color="#7a1f1f", ls="--", lw=0.8)
    side = layout["side_margin_mm"]
    for y in (-y_window + side, y_window - side):
        ax.axhline(y, color="0.35", ls=":", lw=0.8)

    clearance = layout["gap_edge_clearance_mm"]
    ax.annotate(f"один физический зазор g = {gap:.2f} мм".replace(".", ","),
                xy=(0.0, 0.0), xytext=(67.0, 15.0),
                arrowprops=dict(arrowstyle="->", lw=0.8), fontsize=9)
    ax.annotate(f"отступ от кромки зазора = {clearance:.1f} мм".replace(".", ","),
                xy=(x_center + 8.0, keepout), xytext=(67.0, 32.0),
                arrowprops=dict(arrowstyle="->", lw=0.8), fontsize=9)
    ax.set_xlim(-outer / 2.0 - 5.0, outer / 2.0 + 42.0)
    ax.set_ylim(-y_outer - 16.0, y_outer + 5.0)
    ax.set_aspect("equal")
    ax.set_xlabel("ширина, мм")
    ax.set_ylabel("высота, мм")
    ax.set_title(f"Укладка обмотки дросселя фазы, {f_lbl}: {core['name']}, "
                 f"{design['N']} витков, {n_layers} слоя", fontsize=10)
    ax.grid(False)
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def phases_plot(mode_ph, mode_conv, n_phases, f_lbl, path):
    """Фазные токи с равномерным сдвигом и суммарный входной ток.

    Наглядно показывает главное преимущество interleaved: размах суммарного
    тока в K раз меньше размаха тока фазы, а основная частота пульсаций
    определяется числом фаз.
    """
    D = mode_ph["D"]
    f_sw = mode_ph["f_sw_kHz"] * 1e3
    T = 1.0 / f_sw
    i_min, i_max = mode_ph["I_min_A"], mode_ph["I_max_A"]
    n_pts = 2000

    def phase_current(frac, shift):
        x = (frac + shift) % 1.0
        if x < D:
            return i_min + (i_max - i_min) * x / D
        return i_max - (i_max - i_min) * (x - D) / (1.0 - D)

    t = [i / n_pts for i in range(n_pts + 1)]
    ts = [x * T * 1e6 for x in t]
    curves = [[phase_current(x, k / n_phases) for x in t]
              for k in range(n_phases)]
    total = [sum(c[i] for c in curves) for i in range(len(t))]

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.0, 5.0), sharex=True)
    line_styles = ("-", "--", "-.", ":")
    for index, curve in enumerate(curves):
        a1.plot(ts, curve, color="k",
                ls=line_styles[index % len(line_styles)], lw=1.3,
                label=f"фаза {index + 1}")
    a1.set_ylabel("ток фазы, А")
    a1.grid(True, ls=":", lw=0.5)
    a1.legend(fontsize=8, loc="upper right", ncol=min(4, n_phases))
    phase_shift = 360.0 / n_phases
    a1.set_title(f"Токи {n_phases} фаз со сдвигом {phase_shift:g}° и "
                 f"суммарный входной ток, f = {f_lbl}", fontsize=10)
    d_ph = i_max - i_min
    a1.set_ylim(i_min - 0.30 * d_ph, i_max + 0.22 * d_ph)
    a1.annotate(f"ΔI_ф = {d_ph:.3f} А".replace(".", ","),
                xy=(ts[len(ts) // 8], (i_max + i_min) / 2.0),
                xytext=(ts[len(ts) // 8], i_min - 0.20 * d_ph), fontsize=8,
                ha="center", arrowprops=dict(arrowstyle="->", lw=0.7))

    a2.plot(ts, total, "k-", lw=1.4)
    d_in = max(total) - min(total)
    a2.set_ylabel("входной ток, А")
    a2.set_xlabel("время, мкс")
    a2.grid(True, ls=":", lw=0.5)
    mid = (max(total) + min(total)) / 2.0
    a2.set_ylim(mid - 4.0 * d_in, mid + 4.0 * d_in)
    a2.annotate(f"ΔI_вх = {d_in:.4f} А = {d_in/d_ph*100:.1f} % от ΔI_ф; "
                f"частота {mode_conv['f_in_ripple_Hz']/1e3:.0f} кГц"
                .replace(".", ","),
                xy=(ts[len(ts) // 2], max(total)),
                xytext=(ts[len(ts) // 2], mid + 2.4 * d_in), fontsize=8,
                ha="center", arrowprops=dict(arrowstyle="->", lw=0.7))
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def waveform_plot(mode, f_lbl, path):
    """Формы напряжения на дросселе фазы и её тока за один период."""
    D = mode["D"]
    u_in = mode["u_in_V"]
    u_out = mode["u_out_V"]
    f_sw = mode["f_sw_kHz"] * 1e3
    T = 1.0 / f_sw
    I_min, I_max = mode["I_min_A"], mode["I_max_A"]

    t = [T * i / 400.0 for i in range(401)]
    u = [u_in if x < D * T else u_in - u_out for x in t]
    i_l = []
    for x in t:
        if x < D * T:
            i_l.append(I_min + (I_max - I_min) * x / (D * T))
        else:
            i_l.append(I_max - (I_max - I_min) * (x - D * T) / ((1 - D) * T))

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.0, 4.8), sharex=True)
    ts = [x * 1e6 for x in t]
    a1.plot(ts, u, "k-", lw=1.4)
    a1.axhline(0, color="0.6", lw=0.7)
    a1.set_ylabel("u_L, В")
    a1.grid(True, ls=":", lw=0.5)
    a1.set_title(f"Напряжение на дросселе фазы и ток, f = {f_lbl}",
                 fontsize=10)
    a2.plot(ts, i_l, "k-", lw=1.4)
    a2.set_ylabel("i_L, А")
    a2.set_xlabel("время, мкс")
    a2.grid(True, ls=":", lw=0.5)
    a2.set_ylim(I_min - 1.0, I_max + 1.0)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def ripple_vs_D_plot(D_work, n_phases, path):
    """K(D) для нескольких N с отметкой принятого числа фаз."""
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    n_pts = 4000
    ds = [0.001 + 0.998 * i / n_pts for i in range(n_pts + 1)]
    line_styles = ("-", "--", "-.", ":")
    for n_ph in range(1, max(4, n_phases) + 1):
        col = "k" if n_ph == n_phases else "0.55"
        ls = line_styles[(n_ph - 1) % len(line_styles)]
        k = [il.ripple_cancellation_factor(d, n_ph) for d in ds]
        lw = 1.8 if n_ph == n_phases else 1.0
        ax.plot(ds, k, color=col, ls=ls, lw=lw,
                label=f"N = {n_ph}" + (" (принято)" if n_ph == n_phases else ""))
    k_work = il.ripple_cancellation_factor(D_work, n_phases)
    ax.plot([D_work], [k_work], "o", ms=6, mfc="white", mec="k", mew=1.2,
            zorder=5)
    ax.annotate(f"рабочая точка\nD = {D_work:.4f}, K = {k_work:.4f}"
                .replace(".", ","),
                xy=(D_work, k_work), xytext=(D_work + 0.07, 0.42),
                fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
    for index in range(1, n_phases):
        d_zero = index / n_phases
        ax.axvline(d_zero, color="0.7", ls=":", lw=0.8)
        ax.text(d_zero, 1.02, f"D = {index}/{n_phases}", fontsize=8,
                ha="center")
    ax.set_xlabel("коэффициент заполнения D")
    ax.set_ylabel("K = ΔI_вх / ΔI_фазы")
    ax.set_title("Подавление пульсаций входного тока при чередовании фаз",
                 fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.grid(True, ls=":", lw=0.5)
    ax.legend(fontsize=9, loc="upper center")
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def impedance_plot(variants, path):
    """Частотная зависимость |Z(f)| с отметкой первого резонанса."""
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    for idx, (b, lbl, style) in enumerate(variants):
        L = b["design"]["L_min_uH"] * 1e-6
        C = b["design"]["C_self_pF"] * 1e-12
        f = [10.0 ** (4 + 0.005 * i) for i in range(int(3.6 / 0.005) + 1)]
        Z = []
        for fx in f:
            w = 2.0 * math.pi * fx
            den = 1.0 - w * w * L * C
            Z.append(w * L / abs(den) if abs(den) > 1e-12 else 1e9)
        ax.loglog(f, Z, style, lw=1.4, label=lbl)
        f_sw = b["mode"]["f_sw_kHz"] * 1e3
        w_sw = 2.0 * math.pi * f_sw
        ax.plot([f_sw], [w_sw * L / abs(1.0 - w_sw ** 2 * L * C)],
                "o", ms=5, mfc="white", mec="k", mew=1.0, zorder=5)
        f_r = b["design"]["f_res_MHz"] * 1e6
        ax.axvline(f_r, color="0.5", ls=":", lw=0.9)
        y_note = 2.0e2 if idx == 0 else 4.0e1
        ax.annotate(f"f_СР = {b['design']['f_res_MHz']:.2f} МГц "
                    f"({lbl})".replace(".", ","),
                    xy=(f_r, y_note), xytext=(f_r * 1.25, y_note),
                    fontsize=8, va="center",
                    arrowprops=dict(arrowstyle="->", lw=0.7))
    # полоса кондуктивных помех по ГОСТ 30805.22: 150 кГц ... 30 МГц
    ax.axvspan(150e3, 30e6, color="0.85", alpha=0.45, zorder=0)
    # подпись полосы привязана к осевым координатам по вертикали, чтобы не
    # налезать на подпись оси абсцисс при изменении границ графика
    ax.text(math.sqrt(150e3 * 30e6), 0.035,
            "полоса кондуктивных помех 0,15…30 МГц",
            transform=ax.get_xaxis_transform(),
            fontsize=8, ha="center", va="bottom", color="0.25")
    ax.plot([], [], "o", ms=5, mfc="white", mec="k", mew=1.0,
            label="частота коммутации")
    ax.set_ylim(1.0e1, 1.0e6)
    ax.set_xlabel("частота, Гц")
    ax.set_ylabel("модуль импеданса |Z|, Ом")
    ax.set_title("Частотная зависимость импеданса дросселя фазы", fontsize=10)
    ax.grid(True, which="both", ls=":", lw=0.5)
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def main():
    with open(il.JSON_PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    res = data["results"]
    n_phases = int(data["tz"]["n_phases"])
    frequency_rows = []
    for key, result in res.items():
        frequency_hz = result.get("f_sw_Hz")
        if frequency_hz is None:
            frequency_hz = result["selected"]["mode"]["f_sw_kHz"] * 1e3
        value = f"{frequency_hz / 1e3:.6f}".rstrip("0").rstrip(".")
        frequency_rows.append((float(frequency_hz), key,
                               value.replace(".", ",") + " кГц"))
    frequency_rows.sort()
    out = []
    for _, key, lbl in frequency_rows:
        r = res[key]
        b = r["selected"]
        p = os.path.join(IMG_DIR, f"winding_{key}.png")
        winding_layout(b, lbl, p)
        out.append(p)
        p = os.path.join(IMG_DIR, f"waveform_{key}.png")
        waveform_plot(b["mode"], lbl, p)
        out.append(p)
        p = os.path.join(IMG_DIR, f"phases_{key}.png")
        phases_plot(b["mode"], r["mode_converter"], n_phases, lbl, p)
        out.append(p)
    p = os.path.join(IMG_DIR, "ripple_vs_D.png")
    first_key = frequency_rows[0][1]
    ripple_vs_D_plot(res[first_key]["mode_converter"]["D"], n_phases, p)
    out.append(p)
    p = os.path.join(IMG_DIR, "impedance.png")
    styles = ("k-", "k--", "k-.", "k:")
    impedance_plot([(res[key]["selected"], label, styles[index % len(styles)])
                    for index, (_, key, label) in enumerate(frequency_rows)], p)
    out.append(p)
    for x in out:
        print("создан", os.path.relpath(x, ROOT))


if __name__ == "__main__":
    main()
