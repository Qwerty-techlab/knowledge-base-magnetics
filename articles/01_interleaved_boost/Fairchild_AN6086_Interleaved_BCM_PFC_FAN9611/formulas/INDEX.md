# Формулы: Fairchild_AN6086_Interleaved_BCM_PFC_FAN9611

Всего: 39 | страниц просмотрено: 18 | 300 dpi

> Текст в колонке «текстовый слой» приведён только для поиска. Для чтения самой формулы открывать PNG.

| файл | стр. | № | текстовый слой (недостоверно) |
|---|---|---|---|
| `eq_p002_01.png` | 2 | 1 | ( )(( ))INONOUTINOFFVttVVtt⋅=−⋅ (1) |
| `eq_p002_02.png` | 2 | 2 | , ( )11 \| sin(2) \|1 OUTINSW ONOFFONOUT OUTIN PKLINE ONOUT VVtftttV VVft tV π −==⋅+ −⋅=⋅ (2 |
| `eq_p003_01.png` | 3 | - | Figure 5. Minimum Switching Frequency vs. RMS Line Voltage (L = 390µH, POUT = 200W) |
| `eq_p004_01.png` | 4 | 3 | , 21OUTLINESW MIN ONOUT VVftV −=⋅ (3) |
| `eq_p004_02.png` | 4 | 5 | 2LINELINE, , 22 OUTSW MIN OUT CHOUT VVVfPLVη ⋅−=⋅⋅⋅ (5) |
| `eq_p005_01.png` | 5 | 6 | 2,, ,, 2 2 LINE MINFOUTLINE MINF OUT CHSW MINOUT VVVLPfV η ⋅−=⋅⋅⋅ (6) |
| `eq_p005_02.png` | 5 | 7 | ,. , 2 2OUT CHL PK LINE MIN PIVη ⋅=⋅ (7) |
| `eq_p005_03.png` | 5 | 8 | The number of turns of boost inductor should be determined considering the core saturation |
| `eq_p006_01.png` | 6 | 12 | ,2 2(100) ONDDSTART LINE MIN START VCt VARμπ = − (12) |
| `eq_p006_02.png` | 6 | - | Typically 20~50μF of electrolytic capacitor (CVDD2) is used together with 2~4μF of bypass  |
| `eq_p006_03.png` | 6 | 11 | ,2 2100LINE MINSTART START VIARμπ=> (11) |
| `eq_p006_04.png` | 6 | 1 | 11, 2, (1)22 INININ HYS INLINE HYS RRRRVAμ++=⋅ (VAC ) (15) |
| `eq_p006_05.png` | 6 | 16 | .2,112 2()2 LINE HYSININ HYSIN ININ VRRRARRμ=−⋅+ (16) |
| `eq_p007_01.png` | 7 | 18 | 12212, 2230 10()2 ININON MAXMOT INLINE RRtR RV −+=⋅× (18) |
| `eq_p007_02.png` | 7 | 19 | 2 ,,,2 LINEMAX CHMAXOUT CHON MAXVPKPtL η⋅=⋅= (19) |
| `eq_p008_01.png` | 8 | 20 | ,max L PKMAX eBOOST IKLBAN ⋅⋅=⋅ (20) |
| `eq_p008_02.png` | 8 | - | 2 PO MAX=1.7 PO NOMINAL |
| `eq_p009_01.png` | 9 | 23 | ,, ,2 2MAX CHCS LIM LINE MIN PIVη≥⋅⋅ (23) |
| `eq_p009_02.png` | 9 | 24 | . 0.2CS CS LIMRI= (24) |
| `eq_p009_03.png` | 9 | 21 | 2 123FB OUTFBFB RVVRR⋅=+ (21) |
| `eq_p009_04.png` | 9 | 25 | ,2 OUTOUT LINEOUT RIPPLE ICfVπ>⋅⋅ (25) |
| `eq_p009_05.png` | 9 | 26 | 22, 2 OUTHOLDOUT OUTOUT MIN PtC VV ⋅> − (26) |
| `eq_p009_06.png` | 9 | 22 | 2,123.5FB OUT LATCHFBFB RVVRR⋅=+ (22) |
| `eq_p010_01.png` | 10 | 4 | ,(1 cos(4))D AVGOUTLINEIIftπ=−⋅⋅ |
| `eq_p010_02.png` | 10 | - | ,2 OUTOUT RIPPLE LINEOUT IVfCπ= |
| `eq_p010_03.png` | 10 | 27 | , (0.2)4.1 COMPD LFOUTMAX VIIK−=⋅⋅ (27) |
| `eq_p010_04.png` | 10 | 28 | ˆ1ˆ4.1212 OUTOUTMAXL COMP P vIKR sv fπ ⋅=⋅⋅ + (28) where 22P LOUTfR Cπ=⋅ and RL is the out |
| `eq_p010_05.png` | 10 | 29 | @,ˆ1\|ˆ4.1 OUTOUTMAXLIGHT LOADCOMPOUT vIKvsC⋅≅⋅ (29) |
| `eq_p011_01.png` | 11 | 31 | ,280/34.1(2) OUTMAXCOMP LF OUTOUTC A V IKCVCfμ π⋅⋅=⋅⋅⋅ (31) |
| `eq_p011_02.png` | 11 | 32 | , 12COMP CCOMP LFRfCπ=⋅⋅ (32) |
| `eq_p011_03.png` | 11 | 30 | The transfer function of the compensation network is obtained as: 1ˆ22ˆ12 COMPCZI OUT CP s |
| `eq_p011_04.png` | 11 | 33 | , 12COMP HF CPCOMPCfRπ=⋅⋅ (33) |
| `eq_p011_05.png` | 11 | - | ,2 12 SS REFFB FBFBOUT VRRRV=+ |
| `eq_p011_06.png` | 11 | - | , 12CZ COMPCOMP LFfRCπ=⋅ , 12CP COMPCOMP HFfRCπ=⋅ Figure 19. Compensation Network |
| `eq_p012_01.png` | 12 | 34 | , 50.30.6OUTMAXOUTMAX OUTOUTSSSS REFOUTOUT IKIKACVCVCVμ⋅⋅⋅<<⋅⋅⋅⋅ (34) |
| `eq_p012_02.png` | 12 | 35 | ,, 550.60.3 OUTOUTOUTOUTSSOUTMAXSS REFOUTMAXSS REF A CVA CVCIKVIKVμμ⋅⋅⋅⋅<<⋅⋅⋅⋅⋅⋅ (35) |
| `eq_p012_03.png` | 12 | 36 | 2,12tan ()LINE MAXLINEEQ OUT VfC P ηπθ−⋅⋅⋅= (36) |
| `eq_p012_04.png` | 12 | 38 | 12, tan(cos ())2 OUTEQMINLINE MAXLINE PCDFVfηπ −<⋅⋅⋅ (38) |
| `eq_p015_01.png` | 15 | - | (N1:N2=10:1) L1 N2 N1 D1 220uF220uF 200uH (N1:N2=10:1) RURP860 150nF |
