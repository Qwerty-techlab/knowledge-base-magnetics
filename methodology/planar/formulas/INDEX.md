# Формулы самостоятельной методики

Точный LaTeX из исходника. Это не независимая физическая верификация. Номер ниже — порядок извлечения; для ссылок используйте метки. Встроенные формулы остаются в полном документе.

## 1: eq:inductive-voltage

```latex
u_L=u_{\rm term}-u_R,\qquad u_R\simeq R_{\rm DC}(\vartheta)i.
 \label{eq:inductive-voltage}
```

## 2: eq:flux-linkage-voltage

```latex
u_L=\frac{d\psi}{dt},\qquad
 \Delta\psi_{12}=\int_{t_1}^{t_2}u_L(t)\,dt.
 \label{eq:flux-linkage-voltage}
```

## 3: eq:flux-linkage-trajectory

```latex
\psi(t)=\psi(t_0)+\int_{t_0}^{t}u_L(\tau)\,d\tau.
 \label{eq:flux-linkage-trajectory}
```

## 4: eq:current-nonlinear

```latex
L_{\rm diff}=\left.\frac{\partial\psi}{\partial i}\right|_{\vartheta},\qquad
 \frac{di}{dt}=\frac{u_L}{L_{\rm diff}(i,\vartheta)}.
 \label{eq:current-nonlinear}
```

## 5: eq:current-general

```latex
I_{\rm avg}=\frac1{T_s}\int_0^{T_s}i(t)\,dt,\quad
 I_{\rm rms}=\sqrt{\frac1{T_s}\int_0^{T_s}i^2(t)\,dt},\quad I_{\rm pk}=\max_t|i(t)|.
 \label{eq:current-general}
```

## 6: eq:ipeak

```latex
I_{\max}=I_{\rm avg}+\frac{\Delta I_{pp}}2,\qquad
 I_{\rm rms}=\sqrt{I_{\rm avg}^2+\frac{\Delta I_{pp}^2}{12}}.
 \label{eq:ipeak}
```

## 7: eq:energy-linear

```latex
W=\frac12 LI^2.
 \label{eq:energy-linear}
```

## 8: eq:energy-nonlinear

```latex
W(i,\vartheta)=\int_0^{\psi(i,\vartheta)}i(\widetilde\psi,\vartheta)\,d\widetilde\psi.
 \label{eq:energy-nonlinear}
```

## 9: eq:b-equivalent-trajectory

```latex
B_e(t)=\frac{\psi_m(t)}{NA_e},\qquad
 \Delta B_{pp}=B_{e,\max}-B_{e,\min}.
 \label{eq:b-equivalent-trajectory}
```

## 10: eq:b-acceptance

```latex
\max_{r,t,\mathbf x}|B_r(\mathbf x,t)|\leq B_{\rm allow}(\vartheta_{\max}).
 \label{eq:b-acceptance}
```

## 11: pl:eq:ratio-mmf

```latex
a=\frac{N_p}{N_s}=\frac{e_p}{e_s},\qquad
 N_p i_p+N_s i_s=\mathcal F_m .
 \label{pl:eq:ratio-mmf}
```

## 12: pl:eq:matrix-L

```latex
\begin{bmatrix}\psi_p\\\psi_s\end{bmatrix}
 =\begin{bmatrix}L_{pp}&M\\M&L_{ss}\end{bmatrix}
 \begin{bmatrix}i_p\\i_s\end{bmatrix},\qquad
 k=\frac{M}{\sqrt{L_{pp}L_{ss}}}.
 \label{pl:eq:matrix-L}
```

## 13: pl:eq:short-circuit

```latex
L_{\mathrm{sc},p}=L_{pp}-\frac{M^2}{L_{ss}}
                 =L_{pp}(1-k^2).
 \label{pl:eq:short-circuit}
```

## 14: eq:magnetic-circuit

```latex
\mathcal R_m=\sum_j\frac{l_j}{\mu_0\mu_{r,j}A_j}
 +\sum_q\frac{g_q}{\mu_0F_q A_{g,q}},\qquad
 L_m=\frac{N^2}{\mathcal R_m},\qquad A_L=\frac{L_m}{N^2}.
 \label{eq:magnetic-circuit}
```

## 15: eq:gap-fringing

```latex
g^{(n+1)}=\mu_0 A_g F(g^{(n)})
 \left(\frac1{A_{L,\rm target}}-\frac1{A_{L0}}\right).
 \label{eq:gap-fringing}
```

## 16: eq:multiple-gap-balance

```latex
\sum_q\frac{g_q}{F_q A_{g,q}}=
 \mu_0\left(\frac1{A_{L,\rm target}}-\frac1{A_{L0}}\right).
 \label{eq:multiple-gap-balance}
```

## 17: eq:turns-volts

```latex
N_p\geq\frac{\max_t S(t)-\min_t S(t)}{A_e\Delta B_{\rm allow}},
 \qquad S(t)=\int_{t_0}^t e_p(\tau)\,d\tau.
 \label{eq:turns-volts}
```

## 18: eq:igse

```latex
p_v=\frac1{T_s}\int_0^{T_s}k_i\left|\frac{dB}{dt}\right|^\alpha
 (\Delta B_{pp})^{\beta-\alpha}\,dt.
 \label{eq:igse}
```

## 19: eq:igse-coefficient

```latex
k_i=\frac{k}{2^{\beta-\alpha}(2\pi)^{\alpha-1}
 \int_0^{2\pi}|\cos\theta|^\alpha d\theta}.
 \label{eq:igse-coefficient}
```

## 20: eq:core-loss-volume

```latex
P_{\rm Fe}=\int_{V_{\rm Fe}}p_v(\mathbf x)\,dV\simeq p_v V_e.
 \label{eq:core-loss-volume}
```

## 21: pl:eq:height

```latex
h_{\mathrm{stack,max}}+h_{\mathrm{ins,max}}+h_{\mathrm{assembly,max}}
 \leq h_{\mathrm{window,min}}.
 \label{pl:eq:height}
```

## 22: eq:copper-area

```latex
A_{\rm req}=\frac{I_{\rm rms}}{J_0},\qquad
 w_0=\frac{A_{\rm req}}{n_\parallel t_{\min}}.
 \label{eq:copper-area}
```

## 23: eq:rho-temperature

```latex
\rho(\vartheta)=\rho_{20}[1+\alpha_{\rm Cu}(\vartheta-20\,^{\circ}\mathrm C)].
 \label{eq:rho-temperature}
```

## 24: eq:planar-rdc

```latex
R_b=\sum_k\rho_k\frac{l_k}{A_k}+R_{\rm via,b}+R_{\rm joints,b},
 \qquad R_{\rm eq}=\left(\sum_b\frac1{R_b}\right)^{-1}.
 \label{eq:planar-rdc}
```

## 25: eq:via-resistance

```latex
A_v=\frac\pi4[(d_f+2t_v)^2-d_f^2],\quad
 R_v=\frac{\rho l_v}{A_v},\quad R_{\rm group}\simeq\frac{R_v}{n_v}.
 \label{eq:via-resistance}
```

## 26: pl:eq:minimum-section

```latex
w_{\min}=w_{\mathrm{CAD}}-\Delta w_-,\qquad
 A_{\mathrm{Cu,min}}=t_{\min}w_{\min}.
 \label{pl:eq:minimum-section}
```

## 27: pl:eq:trapezoid

```latex
A_{\mathrm{Cu}}=t_{\mathrm{Cu}}\frac{w_{\mathrm{top}}+w_{\mathrm{bottom}}}{2}.
 \label{pl:eq:trapezoid}
```

## 28: pl:eq:radial-fit

```latex
n w_{\mathrm{CAD}}+(n-1)s_{\mathrm{CAD}}+m_{\mathrm{in}}+m_{\mathrm{out}}
 \leq b_{\mathrm{available}}.
 \label{pl:eq:radial-fit}
```

## 29: pl:eq:via-imbalance

```latex
k_{\mathrm{via}}=\frac{\max_r I_{r,\mathrm{rms}}}{I_{\mathrm{group,rms}}/n_v}.
 \label{pl:eq:via-imbalance}
```

## 30: eq:parallel-branch-matrix

```latex
\mathbf Z_b=\mathbf C_s^T\mathbf Z_{\ell}\mathbf C_s,\qquad
 \mathbf i_b=\mathbf Z_b^{-1}\mathbf 1\,U.
 \label{eq:parallel-branch-matrix}
```

## 31: eq:parallel-fixed-current

```latex
\mathbf i_b=\frac{\mathbf Z_b^{-1}\mathbf 1}{\mathbf 1^T\mathbf Z_b^{-1}\mathbf 1}I_{\rm total}.
 \label{eq:parallel-fixed-current}
```

## 32: eq:skin-depth

```latex
\delta(f,\vartheta)=\sqrt{\frac{\rho(\vartheta)}{\pi f\mu_{\rm Cu}}}.
 \label{eq:skin-depth}
```

## 33: eq:copper-loss-harmonic

```latex
P_{\rm Cu}=I_{\rm DC}^2R_{\rm DC}+\sum_{h\geq1}I_{h,\rm rms}^2R_{\rm AC}(f_h).
 \label{eq:copper-loss-harmonic}
```

## 34: eq:metal-eddy-loss

```latex
P_{\rm metal,h}=\int_{V_{\rm metal}}\frac{|\mathbf J_{h,\rm rms}|^2}{\sigma}\,dV.
 \label{eq:metal-eddy-loss}
```

## 35: pl:eq:loss-matrix

```latex
P_{\mathrm{Cu},h}=\mathbf I_h^{\dagger}\,\mathbf R_{\mathrm{Cu},h}\,\mathbf I_h .
 \label{pl:eq:loss-matrix}
```

## 36: eq:capacitance-energy

```latex
W_e=\frac12 C_{\rm eq}U^2=\frac12\int_V\mathbf E\cdot\mathbf D\,dV,
 \qquad C_{\rm eq}=\frac{2W_e}{U^2}.
 \label{eq:capacitance-energy}
```

## 37: eq:common-mode-current

```latex
i_{\rm CM}=C_{\rm CM}\frac{du_{\rm CM}}{dt},\qquad
 I_{{\rm CM},h}=2\pi f_h C_{\rm CM}|U_{{\rm CM},h}|.
 \label{eq:common-mode-current}
```

## 38: eq:impedance

```latex
Z(\omega)=\left[\frac1{R+j\omega L}+j\omega C\right]^{-1},\qquad
 f_{\rm SR}\simeq\frac1{2\pi\sqrt{LC}}.
 \label{eq:impedance}
```

## 39: eq:dielectric-loss-independent

```latex
P_{\rm diel}=\sum_h 2\pi f_h C_h U_{h,\rm rms}^2\tan\delta_{d,h}.
 \label{eq:dielectric-loss-independent}
```

## 40: pl:eq:plate-capacitance

```latex
C_{ij}^{(0)}=\varepsilon_0\varepsilon_{r,ij}\frac{A_{ij}}{d_{ij}}.
 \label{pl:eq:plate-capacitance}
```

## 41: eq:mesh-convergence

```latex
\varepsilon_Q=\frac{|Q_m-Q_{m-1}|}{\max(|Q_m|,Q_{\rm floor})}.
 \label{eq:mesh-convergence}
```

## 42: eq:fem-energy-check

```latex
W_{\rm field}\simeq\frac12\mathbf i^T\mathbf L\mathbf i
 \quad\text{(для одной обмотки: }W_{\rm field}\simeq LI^2/2\text{)}.
 \label{eq:fem-energy-check}
```

## 43: eq:heat-density

```latex
q_{v,k}=P_k/V_k,\qquad \Delta\vartheta=P_\Sigma R_\theta.
 \label{eq:heat-density}
```

## 44: eq:thermal-pde

```latex
\rho_m c_p\frac{\partial\vartheta}{\partial t}
 =\nabla\cdot(\mathbf K\nabla\vartheta)+q_v.
 \label{eq:thermal-pde}
```

## 45: eq:mission-profile-loss

```latex
\overline P_\Sigma=\sum_r w_rP_{\Sigma,r},\qquad
 w_r\geq0,\quad\sum_r w_r=1.
 \label{eq:mission-profile-loss}
```
