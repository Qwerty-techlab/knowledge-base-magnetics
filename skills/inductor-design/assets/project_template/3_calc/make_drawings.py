# -*- coding: utf-8 -*-
"""Иллюстрации для отчёта об одном boost-дросселе с одним зазором."""
from __future__ import annotations

import json
import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
IMG_DIR = os.path.join(PROJECT_ROOT, "1_output_files", "img")
RESULTS = os.path.join(HERE, "results_single_gap.json")

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})


def _selected_results(payload):
    rows = [(key, value["selected"]) for key, value in payload["results"].items()
            if value.get("status") == "analytical_solution"]
    return sorted(rows, key=lambda item: item[1]["mode"]["f_sw_kHz"])


def _frequency_label(selected):
    value = f"{selected['mode']['f_sw_kHz']:.6f}".rstrip("0").rstrip(".")
    return value.replace(".", ",") + " кГц"


def winding_layout(selected, label, path):
    """Фронтальное сечение комплекта сердечника с укладкой кабелей."""

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
    clearance = layout["gap_edge_clearance_mm"]
    keepout = layout["gap_keepout_half_mm"]
    group_radial = layout["group_radial_mm"]
    radial_step = group_radial + layout["interlayer_insulation_mm"]
    turn_pitch = layout["turn_pitch_mm"]
    n_turns = int(design["N"])

    remaining = n_turns
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

    clr = layout["gap_edge_clearance_mm"]
    for y in (-keepout, keepout):
        ax.axhline(y, color="#7a1f1f", ls="--", lw=0.8)
    side = layout.get("side_margin_mm", layout.get("side_mmargin_mm", 0.05 * window_h))
    for y in (-y_window + side, y_window - side):
        ax.axhline(y, color="0.35", ls=":", lw=0.8)

    ax.annotate(f"один зазор g = {gap:.2f} мм".replace(".", ","),
                xy=(0.0, 0.0), xytext=(67.0, 5.0),
                arrowprops=dict(arrowstyle="->", lw=0.8), fontsize=9)
    ax.annotate(f"отступ меди r_g = {clr:.1f} мм".replace(".", ","),
                xy=(x_center + 8.0, keepout), xytext=(67.0, 25.0),
                arrowprops=dict(arrowstyle="->", lw=0.8), fontsize=9)
    ax.set_xlim(-outer / 2.0 - 5.0, outer / 2.0 + 42.0)
    ax.set_ylim(-y_outer - 16.0, y_outer + 5.0)
    ax.set_aspect("equal")
    ax.set_xlabel("ширина, мм")
    ax.set_ylabel("высота, мм")
    ax.set_title(f"Расчётная укладка обмотки, {label}: {core['name']}")
    ax.grid(False)
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def waveform_plot(selected, label, path):
    mode = selected["mode"]
    D = mode["D"]
    f_sw = mode["f_sw_kHz"] * 1e3
    period = 1.0 / f_sw
    u_in = mode["u_in_V"]
    u_out = mode["u_out_V"]
    i_min = mode["I_min_A"]
    i_max = mode["I_max_A"]
    time = [period * index / 500.0 for index in range(501)]
    voltage = [u_in if value < D * period else u_in - u_out for value in time]
    current = []
    for value in time:
        if value < D * period:
            current.append(i_min + (i_max - i_min) * value / (D * period))
        else:
            current.append(i_max - (i_max - i_min) *
                           (value - D * period) / ((1.0 - D) * period))

    fig, axes = plt.subplots(2, 1, figsize=(7.2, 4.8), sharex=True)
    time_us = [value * 1e6 for value in time]
    axes[0].plot(time_us, voltage, "k-", lw=1.3)
    axes[0].axhline(0.0, color="0.6", lw=0.7)
    axes[0].set_ylabel("u_L, В")
    axes[0].grid(True, ls=":", lw=0.5)
    axes[1].plot(time_us, current, "k-", lw=1.3)
    axes[1].set_ylabel("i_L, А")
    axes[1].set_xlabel("время, мкс")
    axes[1].grid(True, ls=":", lw=0.5)
    axes[0].set_title(f"Номинальные формы напряжения и тока, {label}")
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def impedance_plot(results, path):
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    styles = ("k-", "k--")
    for index, (key, selected) in enumerate(results):
        design = selected["design"]
        L = design["L_min_uH"] * 1e-6
        C = design["C_self_pF"] * 1e-12
        frequencies = [10.0 ** (4.0 + 0.005 * value) for value in range(721)]
        impedance = []
        for frequency in frequencies:
            omega = 2.0 * math.pi * frequency
            den = abs(1.0 - omega ** 2 * L * C)
            impedance.append(omega * L / max(den, 1e-12))
        label = _frequency_label(selected)
        ax.loglog(frequencies, impedance, styles[index % len(styles)],
                  lw=1.3, label=label)
        ax.axvline(design["f_res_MHz"] * 1e6, color="0.55", ls=":", lw=0.8)
    ax.axvspan(150e3, 30e6, color="0.88", alpha=0.5)
    ax.set_xlabel("частота, Гц")
    ax.set_ylabel("модуль импеданса |Z|, Ом")
    ax.set_title("Предварительная частотная модель дросселя")
    ax.grid(True, which="both", ls=":", lw=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=220)
    plt.close(fig)


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    with open(RESULTS, encoding="utf-8") as stream:
        payload = json.load(stream)
    results = _selected_results(payload)
    created = []
    for key, selected in results:
        label = _frequency_label(selected)
        path = os.path.join(IMG_DIR, f"winding_{key}.png")
        winding_layout(selected, label, path)
        created.append(path)
        path = os.path.join(IMG_DIR, f"waveform_{key}.png")
        waveform_plot(selected, label, path)
        created.append(path)
    path = os.path.join(IMG_DIR, "impedance.png")
    impedance_plot(results, path)
    created.append(path)
    for value in created:
        print("создан", value)


if __name__ == "__main__":
    main()
