# Hard Talkchess
The epd of this test suite is in the docs/2020 folder.

### A. Engine Ranking

```
+----+----------------------+------------+---------------+-------------+------------------------------+----------------+-----------+
|    | name                 |   numsolve |   meantimesec |   pospersec | cpu                          | gpu            |   threads |
|----+----------------------+------------+---------------+-------------+------------------------------+----------------+-----------|
|  0 | Bluefish-FD-XI-DC    |        191 |            25 |           5 | AMD Ryzen Threadripper 3970X | na             |         2 |
|  1 | Bluefish-FD-XI-TD    |        181 |           153 |          30 | i7-4930K                     | na             |         1 |
|  2 | Eman_5.40_fad_12     |        167 |           193 |          30 | i7-4930K                     | na             |         1 |
|  3 | SugaR.AI.ICCF.1.00   |        166 |           113 |          30 | i7-4930K                     | na             |         1 |
|  4 | ShashChess15.1       |        166 |           170 |          30 | i7-4930K                     | na             |         1 |
|  5 | Bluefish-12-W        |        162 |           187 |          30 | i7-4930K                     | na             |         1 |
|  6 | Crystal-2020-06-29   |        159 |           199 |          30 | i7-4930K                     | na             |         1 |
|  7 | Bluefish-XI          |        159 |           222 |          30 | i7-4930K                     | na             |         1 |
|  8 | CorChess v6          |        156 |           327 |          30 | i7-4930K                     | na             |         1 |
|  9 | Houdidi_6.03_tac_1   |        155 |           196 |          30 | i7-4930K                     | na             |         1 |
| 10 | Stockfish_2020-07-19 |        155 |           239 |          30 | i7-4930K                     | na             |         1 |
| 11 | ShashChess 12.1      |        154 |           248 |          30 | i7-4930K                     | na             |         1 |
| 12 | Stockfish_20121407   |        153 |           229 |          30 | i7-4930K                     | na             |         1 |
| 13 | Stockfish_20062710   |        153 |           331 |          30 | i7-4930K                     | na             |         1 |
| 14 | Eman 6.61            |        153 |           258 |          30 | i7-4930K                     | na             |         1 |
| 15 | SugaR.AI.1.00        |        149 |           280 |          30 | i7-4930K                     | na             |         1 |
| 16 | Stockfish 11         |        141 |           366 |          30 | i7-4930K                     | na             |         1 |
| 17 | Honey-XI             |        139 |           290 |          30 | i7-4930K                     | na             |         1 |
| 18 | Stockfish 10         |        137 |           450 |          30 | i7-4930K                     | na             |         1 |
| 19 | Black-Diamond-XI     |        136 |           267 |          30 | i7-4930K                     | na             |         1 |
| 20 | Black-Diamond-XR7    |        136 |           231 |          30 | i7-4930K                     | na             |         1 |
| 21 | Crystal 2020-05-02   |        136 |           187 |          30 | i7-4930K                     | na             |         1 |
| 22 | Crystal 1.1          |        135 |           270 |          30 | i7-4930K                     | na             |         1 |
| 23 | Black-Diamond-XI-r2  |        135 |           158 |          30 | i7-4930K                     | na             |         1 |
| 24 | McCain-v2            |        130 |           389 |          30 | i7-4930K                     | na             |         1 |
| 25 | Stockfish 9          |        130 |           473 |          30 | i7-4930K                     | na             |         1 |
| 26 | Houdidi_6.03_tac_def |        125 |           349 |          30 | i7-4930K                     | na             |         1 |
| 27 | Lc0 v0.26.3 s1       |        123 |            10 |           2 | i7-2600K                     | GTX 1650 super |         2 |
| 28 | Sting-SF-16          |        122 |           234 |          30 | i7-4930K                     | na             |         1 |
| 29 | Sting-SF-20          |        119 |           240 |          30 | i7-4930K                     | na             |         1 |
| 30 | Ethereal 12.25       |         98 |           396 |          30 | i7-4930K                     | na             |         1 |
| 31 | Houdini 1.5 x64      |         97 |           283 |          30 | i7-4930K                     | na             |         1 |
| 32 | Critter 1.6a 64bit   |         96 |           240 |          30 | i7-4930K                     | na             |         1 |
| 33 | Stockfish 8          |         94 |           507 |          30 | i7-4930K                     | na             |         1 |
| 34 | Xiphos 0.6           |         81 |           330 |          30 | i7-4930K                     | na             |         1 |
| 35 | Ethereal 11.75       |         77 |           613 |          30 | i7-4930K                     | na             |         1 |
| 36 | Stockfish 7          |         76 |           487 |          30 | i7-4930K                     | na             |         1 |
+----+----------------------+------------+---------------+-------------+------------------------------+----------------+-----------+
```


##### Header Legend
```
Stockfish_2020-07-19: Stockfish.sse42.halfkp_256x2-32-32.Profile-nnue.2020-07-19
Bluefish-FD-XI-DC: Bluefish-FD-XI-T=2;D=N;DC 3970X 5 minutes
Bluefish-FD-XI-TD: Bluefish-FD-XI-(Tact=2,defens=no)
Houdidi_6.03_tac_1: Houdidit603-tact=1
Houdidi_6.03_tac_def: Houdidit603(default)
Eman_5.40_fad_12: Eman 5.40, FAD=12
Lc0 v0.26.3 s1: Lc0 v0.26.3 cudnn-fp16, 66680, GTX 1650 super, i7-2600K, 2 minutes/pos
```

### B. Hard Ranking
```
+-----+-------------------+---------------------+---------------+
|     | Solution          |   NumEngSolvedCount |   MeanTimeSec |
|-----+-------------------+---------------------+---------------|
|   0 | 23) Nf3-h4        |                   0 |           nan |
|   1 | 33) Nf7-d6        |                   2 |           964 |
|   2 | 102) h5xg6        |                   3 |           497 |
|   3 | 38) Ne4-c3        |                   4 |           524 |
|   4 | 74) Kb7-c8        |                   4 |           324 |
|   5 | 7) Rh4xh1         |                   4 |            54 |
|   6 | 77) Nc4-a5        |                   5 |           382 |
|   7 | 57) Nc2-d4        |                   5 |           193 |
|   8 | 68) Qc7-d8        |                   6 |           379 |
|   9 | 67) f3-f4         |                   6 |           322 |
|  10 | 204) Bc1-g5       |                   6 |           215 |
|  11 | 91) Be3xc5        |                   6 |           114 |
|  12 | 26) Ne2-f4        |                   7 |           936 |
|  13 | 184) .. Bf5-g4    |                   7 |           884 |
|  14 | 78) Qd6xe5        |                   7 |           638 |
|  15 | 131) Na8-c7       |                   7 |           626 |
|  16 | 153) Ne2-d4       |                   7 |           232 |
|  17 | 18) Be1-d2        |                   7 |           148 |
|  18 | 130) f2-f4        |                   8 |           364 |
|  19 | 70) a7-a8B        |                   8 |           337 |
|  20 | 89) .. Re2xd2     |                   8 |           282 |
|  21 | 69) Re8xe5        |                   8 |           116 |
|  22 | 93) Nc6xe7        |                   8 |            53 |
|  23 | 150) Bd4-f6       |                   9 |           967 |
|  24 | 99) .. Qd3xg3     |                   9 |           730 |
|  25 | 144) Bg5-f6       |                   9 |           508 |
|  26 | 95) Kg2-f3        |                   9 |           397 |
|  27 | 80) Bh6-g5        |                   9 |            49 |
|  28 | 177) Nf3-h4       |                  10 |           501 |
|  29 | 51) b4-b5         |                  10 |           216 |
|  30 | 39) .. Rd6-f6     |                  11 |           563 |
|  31 | 3) Nb8-c6         |                  11 |           509 |
|  32 | 208) Bd3xh7       |                  11 |           237 |
|  33 | 58) Ng5xf7        |                  11 |           228 |
|  34 | 126) Nd4-c6       |                  12 |           653 |
|  35 | 113) Ng4-f6       |                  12 |           550 |
|  36 | 14) Qf4-f6        |                  12 |           412 |
|  37 | 108) Be2-h5       |                  12 |           267 |
|  38 | 19) Ng3-f5        |                  13 |           662 |
|  39 | 209) Bc1-d2       |                  13 |           249 |
|  40 | 195) .. Rh6xh2    |                  13 |           236 |
|  41 | 141) Ra3-c3       |                  13 |           111 |
|  42 | 21) .. Rb8xb3     |                  13 |            35 |
|  43 | 97) .. Qh5-f5     |                  14 |           505 |
|  44 | 138) Qh4-d4       |                  14 |           283 |
|  45 | 11) g2-g4         |                  14 |           215 |
|  46 | 170) Qf3-f6       |                  15 |           662 |
|  47 | 8) Rd4-d6         |                  15 |           615 |
|  48 | 158) Na3-b5       |                  15 |           444 |
|  49 | 105) Ne7-c8       |                  15 |           418 |
|  50 | 73) .. e6-e5      |                  15 |           276 |
|  51 | 101) Kh4-h5       |                  15 |           165 |
|  52 | 76) .. Rh7xh4     |                  15 |            87 |
|  53 | 133) Bh5-f3       |                  16 |           396 |
|  54 | 54) Bc2-a4        |                  16 |           241 |
|  55 | 90) Bd6-f8        |                  16 |           216 |
|  56 | 176) d5-d6        |                  17 |           475 |
|  57 | 13) .. Nb6-c4     |                  17 |           471 |
|  58 | 43) Ne5-g6        |                  18 |           608 |
|  59 | 15) h2-h4         |                  18 |           549 |
|  60 | 117) .. Rc5-b5(?) |                  18 |           519 |
|  61 | 156) f4-f5        |                  18 |           480 |
|  62 | 169) Bd3xh7       |                  18 |           396 |
|  63 | 116) Nf4-d3       |                  18 |           383 |
|  64 | 83) d4-d5         |                  18 |           369 |
|  65 | 125) Ne3-g2       |                  18 |           263 |
|  66 | 181) h2-h4        |                  18 |           217 |
|  67 | 20) a4-a5         |                  19 |           469 |
|  68 | 34) f5-f6         |                  19 |           389 |
|  69 | 179) .. Rd8xd4    |                  19 |           217 |
|  70 | 28) Ra4-a2        |                  19 |           178 |
|  71 | 53) Bg5-f4        |                  19 |           101 |
|  72 | 1) Ne7-c6         |                  20 |           559 |
|  73 | 155) Bd3-g6       |                  20 |           407 |
|  74 | 27) Re3-e8        |                  20 |           306 |
|  75 | 135) Bd8-c7       |                  20 |           289 |
|  76 | 103) Qa3-h3       |                  20 |           257 |
|  77 | 196) Nc3-d5       |                  21 |           605 |
|  78 | 164) .. Bb4xa3(?) |                  21 |           459 |
|  79 | 200) Bg3-f4       |                  21 |           413 |
|  80 | 65) .. Ba6-c8     |                  21 |           409 |
|  81 | 87) c7-c8N        |                  21 |           300 |
|  82 | 24) Rc1xc3        |                  21 |           285 |
|  83 | 114) Ne5xd3       |                  21 |           162 |
|  84 | 79) Bd3xg6        |                  21 |           138 |
|  85 | 44) g3-g4         |                  22 |           467 |
|  86 | 36) Kd2-c1        |                  22 |           439 |
|  87 | 2) Qf3xf6         |                  22 |           431 |
|  88 | 123) Ke5-f6       |                  22 |           293 |
|  89 | 178) Bc1-g5       |                  22 |           151 |
|  90 | 140) Be3-d4       |                  22 |            99 |
|  91 | 182) Ng3-h5       |                  23 |           669 |
|  92 | 59) Ne3-f5        |                  23 |           510 |
|  93 | 66) .. e5-e4      |                  23 |           302 |
|  94 | 185) .. Kg8-g7    |                  23 |           286 |
|  95 | 192) Qe2xd2, Ne5- |                  24 |           532 |
|  96 | 190) Qe2-h5       |                  24 |           357 |
|  97 | 6) b3-b4          |                  24 |           324 |
|  98 | 47) Rf2-f4        |                  24 |           300 |
|  99 | 118) .. Re7-a7    |                  24 |           247 |
| 100 | 98) .. Re3xf3     |                  24 |           232 |
| 101 | 109) Bc4-e2       |                  24 |           224 |
| 102 | 46) Qg3xe5        |                  24 |           174 |
| 103 | 211) Qd1-f3       |                  24 |           173 |
| 104 | 160) Ne4-g5       |                  25 |           408 |
| 105 | 194) .. e4-e3     |                  25 |           228 |
| 106 | 64) Kc3-d4        |                  25 |           192 |
| 107 | 61) .. f4-f3      |                  26 |           472 |
| 108 | 154) Nd4-f3       |                  26 |           471 |
| 109 | 163) Qe2xe8       |                  26 |           323 |
| 110 | 187) Ba4xc6       |                  26 |           280 |
| 111 | 48) Bd3xh7        |                  26 |           271 |
| 112 | 136) Kb5-a6       |                  26 |           254 |
| 113 | 10) Rd6xf6        |                  26 |           171 |
| 114 | 56) Ne5xg6        |                  27 |           511 |
| 115 | 159) Bd3xh7       |                  27 |           292 |
| 116 | 37) Re1-e6        |                  27 |           271 |
| 117 | 49) Kh2-g3        |                  27 |           223 |
| 118 | 129) Bb4-a5       |                  27 |           198 |
| 119 | 172) Rd1-d3       |                  27 |            72 |
| 120 | 42) b2-b4         |                  27 |            62 |
| 121 | 35) Qe3xg5        |                  28 |           429 |
| 122 | 119) h4-h5        |                  28 |           416 |
| 123 | 110) Kf2-e1       |                  28 |           398 |
| 124 | 189) Qf3xf4       |                  28 |           397 |
| 125 | 12) Rg1xg7        |                  28 |           348 |
| 126 | 29) e4-e5         |                  28 |           264 |
| 127 | 16) Bd3xh7        |                  28 |           208 |
| 128 | 75) Rd7-d2        |                  28 |           197 |
| 129 | 122) .. Bf5-h3    |                  28 |           179 |
| 130 | 60) Nh3-g5        |                  28 |           109 |
| 131 | 104) b7-b8R       |                  28 |           102 |
| 132 | 111) .. e4-e3     |                  28 |            79 |
| 133 | 88) Qf5-e6        |                  28 |            53 |
| 134 | 165) b6-b7        |                  29 |           603 |
| 135 | 81) Rg2xg7        |                  29 |           481 |
| 136 | 148) Bd3xh7       |                  29 |           304 |
| 137 | 157) Kg1-f2       |                  29 |           298 |
| 138 | 85) h5-h6         |                  29 |           282 |
| 139 | 203) g2-g3        |                  29 |           182 |
| 140 | 52) Bd5xf7        |                  29 |           163 |
| 141 | 121) Na5-b3       |                  29 |           157 |
| 142 | 25) e4-e5         |                  29 |           138 |
| 143 | 41) c4-c5         |                  29 |           102 |
| 144 | 120) c3-c4        |                  29 |            70 |
| 145 | 127) .. Nb6xc4    |                  30 |           495 |
| 146 | 197) .. Qb2-c2    |                  30 |           433 |
| 147 | 100) a5-a6        |                  30 |           371 |
| 148 | 152) Rd1xd7       |                  30 |           282 |
| 149 | 198) Ne7-d5       |                  30 |           264 |
| 150 | 94) b3-b4         |                  30 |           174 |
| 151 | 5) Qc1-h6         |                  30 |           159 |
| 152 | 149) Bd3xh7       |                  30 |            75 |
| 153 | 147) Rd1-d8       |                  31 |           501 |
| 154 | 31) Rc8xc7        |                  31 |           328 |
| 155 | 146) Rd1-d8       |                  31 |           295 |
| 156 | 167) Nd5-f6       |                  31 |           266 |
| 157 | 212) Qe3-d3       |                  31 |           206 |
| 158 | 72) g5-g6         |                  31 |           168 |
| 159 | 202) e5-e6        |                  31 |           147 |
| 160 | 55) Qd8-a8        |                  31 |           134 |
| 161 | 22) g2-g4         |                  31 |            82 |
| 162 | 30) Rf1xf6        |                  31 |            57 |
| 163 | 171) Qf3-f6       |                  32 |           495 |
| 164 | 62) .. Qg5xg3     |                  32 |           334 |
| 165 | 206) Rf1-f6       |                  32 |           304 |
| 166 | 183) Ne3-g4       |                  32 |           267 |
| 167 | 50) Rf1-f5        |                  32 |           250 |
| 168 | 186) Rf3-f6       |                  32 |           199 |
| 169 | 124) Ke2-d3       |                  32 |           190 |
| 170 | 180) .. O-O-O     |                  32 |           190 |
| 171 | 96) Nc3-d5        |                  32 |           169 |
| 172 | 134) Rh1-h6       |                  32 |           157 |
| 173 | 174) g2-g4        |                  32 |           130 |
| 174 | 84) Rd3xb3        |                  32 |           121 |
| 175 | 151) Bd3xh7       |                  32 |           119 |
| 176 | 112) Rf1-c1       |                  32 |            55 |
| 177 | 191) Bd3xh7       |                  33 |           305 |
| 178 | 45) Qc6-f3        |                  33 |           293 |
| 179 | 4) e4-e5          |                  33 |           201 |
| 180 | 106) .. Rd7xd4    |                  33 |           157 |
| 181 | 17) Nf3-g5        |                  33 |           151 |
| 182 | 32) Ng3-h5        |                  33 |           114 |
| 183 | 115) Rf4-g4       |                  33 |            98 |
| 184 | 82) Ng7-f5        |                  33 |            86 |
| 185 | 213) Ng5xf7       |                  34 |           536 |
| 186 | 166) Nf8-g6       |                  34 |           387 |
| 187 | 132) .. Qe4xc4    |                  34 |           297 |
| 188 | 201) Bd3xh7       |                  34 |           255 |
| 189 | 175) Nd4-c6       |                  34 |           197 |
| 190 | 173) Qg5-h6       |                  34 |           195 |
| 191 | 142) Bf1-e2       |                  34 |           193 |
| 192 | 207) .. Ne4-d6    |                  34 |           192 |
| 193 | 63) h4-h5         |                  34 |           107 |
| 194 | 107) f4-f5        |                  34 |            84 |
| 195 | 210) Qd1-h5       |                  35 |           312 |
| 196 | 139) .. Ne8-c7    |                  35 |           271 |
| 197 | 199) d5-d6        |                  35 |           251 |
| 198 | 168) Nd5-f6       |                  35 |           207 |
| 199 | 71) .. h7-h5      |                  35 |           163 |
| 200 | 137) .. Nf6-h5    |                  35 |           160 |
| 201 | 92) .. Bb7-d5     |                  35 |           115 |
| 202 | 40) Kh3-g2        |                  35 |            95 |
| 203 | 162) Rh1xh7       |                  35 |            33 |
| 204 | 205) Rd1-g1       |                  36 |           295 |
| 205 | 193) .. c3xb2     |                  36 |           234 |
| 206 | 188) Rd3-h3       |                  36 |           163 |
| 207 | 161) Bd3xh7       |                  36 |            96 |
| 208 | 145) Rd1-d8       |                  36 |            94 |
| 209 | 143) Re1xe7       |                  36 |            57 |
| 210 | 86) c2-c4         |                  36 |            42 |
| 211 | 128) Bb2-a3       |                  36 |            21 |
| 212 | 9) Bd3xh7         |                  36 |            12 |
+-----+-------------------+---------------------+---------------+
```

### C. Easy Ranking
```
+-----+-------------------+---------------------+---------------+
|     | Solution          |   NumEngSolvedCount |   MeanTimeSec |
|-----+-------------------+---------------------+---------------|
|   0 | 9) Bd3xh7         |                  36 |            12 |
|   1 | 128) Bb2-a3       |                  36 |            21 |
|   2 | 86) c2-c4         |                  36 |            42 |
|   3 | 143) Re1xe7       |                  36 |            57 |
|   4 | 145) Rd1-d8       |                  36 |            94 |
|   5 | 161) Bd3xh7       |                  36 |            96 |
|   6 | 188) Rd3-h3       |                  36 |           163 |
|   7 | 193) .. c3xb2     |                  36 |           234 |
|   8 | 205) Rd1-g1       |                  36 |           295 |
|   9 | 162) Rh1xh7       |                  35 |            33 |
|  10 | 40) Kh3-g2        |                  35 |            95 |
|  11 | 92) .. Bb7-d5     |                  35 |           115 |
|  12 | 137) .. Nf6-h5    |                  35 |           160 |
|  13 | 71) .. h7-h5      |                  35 |           163 |
|  14 | 168) Nd5-f6       |                  35 |           207 |
|  15 | 199) d5-d6        |                  35 |           251 |
|  16 | 139) .. Ne8-c7    |                  35 |           271 |
|  17 | 210) Qd1-h5       |                  35 |           312 |
|  18 | 107) f4-f5        |                  34 |            84 |
|  19 | 63) h4-h5         |                  34 |           107 |
|  20 | 207) .. Ne4-d6    |                  34 |           192 |
|  21 | 142) Bf1-e2       |                  34 |           193 |
|  22 | 173) Qg5-h6       |                  34 |           195 |
|  23 | 175) Nd4-c6       |                  34 |           197 |
|  24 | 201) Bd3xh7       |                  34 |           255 |
|  25 | 132) .. Qe4xc4    |                  34 |           297 |
|  26 | 166) Nf8-g6       |                  34 |           387 |
|  27 | 213) Ng5xf7       |                  34 |           536 |
|  28 | 82) Ng7-f5        |                  33 |            86 |
|  29 | 115) Rf4-g4       |                  33 |            98 |
|  30 | 32) Ng3-h5        |                  33 |           114 |
|  31 | 17) Nf3-g5        |                  33 |           151 |
|  32 | 106) .. Rd7xd4    |                  33 |           157 |
|  33 | 4) e4-e5          |                  33 |           201 |
|  34 | 45) Qc6-f3        |                  33 |           293 |
|  35 | 191) Bd3xh7       |                  33 |           305 |
|  36 | 112) Rf1-c1       |                  32 |            55 |
|  37 | 151) Bd3xh7       |                  32 |           119 |
|  38 | 84) Rd3xb3        |                  32 |           121 |
|  39 | 174) g2-g4        |                  32 |           130 |
|  40 | 134) Rh1-h6       |                  32 |           157 |
|  41 | 96) Nc3-d5        |                  32 |           169 |
|  42 | 124) Ke2-d3       |                  32 |           190 |
|  43 | 180) .. O-O-O     |                  32 |           190 |
|  44 | 186) Rf3-f6       |                  32 |           199 |
|  45 | 50) Rf1-f5        |                  32 |           250 |
|  46 | 183) Ne3-g4       |                  32 |           267 |
|  47 | 206) Rf1-f6       |                  32 |           304 |
|  48 | 62) .. Qg5xg3     |                  32 |           334 |
|  49 | 171) Qf3-f6       |                  32 |           495 |
|  50 | 30) Rf1xf6        |                  31 |            57 |
|  51 | 22) g2-g4         |                  31 |            82 |
|  52 | 55) Qd8-a8        |                  31 |           134 |
|  53 | 202) e5-e6        |                  31 |           147 |
|  54 | 72) g5-g6         |                  31 |           168 |
|  55 | 212) Qe3-d3       |                  31 |           206 |
|  56 | 167) Nd5-f6       |                  31 |           266 |
|  57 | 146) Rd1-d8       |                  31 |           295 |
|  58 | 31) Rc8xc7        |                  31 |           328 |
|  59 | 147) Rd1-d8       |                  31 |           501 |
|  60 | 149) Bd3xh7       |                  30 |            75 |
|  61 | 5) Qc1-h6         |                  30 |           159 |
|  62 | 94) b3-b4         |                  30 |           174 |
|  63 | 198) Ne7-d5       |                  30 |           264 |
|  64 | 152) Rd1xd7       |                  30 |           282 |
|  65 | 100) a5-a6        |                  30 |           371 |
|  66 | 197) .. Qb2-c2    |                  30 |           433 |
|  67 | 127) .. Nb6xc4    |                  30 |           495 |
|  68 | 120) c3-c4        |                  29 |            70 |
|  69 | 41) c4-c5         |                  29 |           102 |
|  70 | 25) e4-e5         |                  29 |           138 |
|  71 | 121) Na5-b3       |                  29 |           157 |
|  72 | 52) Bd5xf7        |                  29 |           163 |
|  73 | 203) g2-g3        |                  29 |           182 |
|  74 | 85) h5-h6         |                  29 |           282 |
|  75 | 157) Kg1-f2       |                  29 |           298 |
|  76 | 148) Bd3xh7       |                  29 |           304 |
|  77 | 81) Rg2xg7        |                  29 |           481 |
|  78 | 165) b6-b7        |                  29 |           603 |
|  79 | 88) Qf5-e6        |                  28 |            53 |
|  80 | 111) .. e4-e3     |                  28 |            79 |
|  81 | 104) b7-b8R       |                  28 |           102 |
|  82 | 60) Nh3-g5        |                  28 |           109 |
|  83 | 122) .. Bf5-h3    |                  28 |           179 |
|  84 | 75) Rd7-d2        |                  28 |           197 |
|  85 | 16) Bd3xh7        |                  28 |           208 |
|  86 | 29) e4-e5         |                  28 |           264 |
|  87 | 12) Rg1xg7        |                  28 |           348 |
|  88 | 189) Qf3xf4       |                  28 |           397 |
|  89 | 110) Kf2-e1       |                  28 |           398 |
|  90 | 119) h4-h5        |                  28 |           416 |
|  91 | 35) Qe3xg5        |                  28 |           429 |
|  92 | 42) b2-b4         |                  27 |            62 |
|  93 | 172) Rd1-d3       |                  27 |            72 |
|  94 | 129) Bb4-a5       |                  27 |           198 |
|  95 | 49) Kh2-g3        |                  27 |           223 |
|  96 | 37) Re1-e6        |                  27 |           271 |
|  97 | 159) Bd3xh7       |                  27 |           292 |
|  98 | 56) Ne5xg6        |                  27 |           511 |
|  99 | 10) Rd6xf6        |                  26 |           171 |
| 100 | 136) Kb5-a6       |                  26 |           254 |
| 101 | 48) Bd3xh7        |                  26 |           271 |
| 102 | 187) Ba4xc6       |                  26 |           280 |
| 103 | 163) Qe2xe8       |                  26 |           323 |
| 104 | 154) Nd4-f3       |                  26 |           471 |
| 105 | 61) .. f4-f3      |                  26 |           472 |
| 106 | 64) Kc3-d4        |                  25 |           192 |
| 107 | 194) .. e4-e3     |                  25 |           228 |
| 108 | 160) Ne4-g5       |                  25 |           408 |
| 109 | 211) Qd1-f3       |                  24 |           173 |
| 110 | 46) Qg3xe5        |                  24 |           174 |
| 111 | 109) Bc4-e2       |                  24 |           224 |
| 112 | 98) .. Re3xf3     |                  24 |           232 |
| 113 | 118) .. Re7-a7    |                  24 |           247 |
| 114 | 47) Rf2-f4        |                  24 |           300 |
| 115 | 6) b3-b4          |                  24 |           324 |
| 116 | 190) Qe2-h5       |                  24 |           357 |
| 117 | 192) Qe2xd2, Ne5- |                  24 |           532 |
| 118 | 185) .. Kg8-g7    |                  23 |           286 |
| 119 | 66) .. e5-e4      |                  23 |           302 |
| 120 | 59) Ne3-f5        |                  23 |           510 |
| 121 | 182) Ng3-h5       |                  23 |           669 |
| 122 | 140) Be3-d4       |                  22 |            99 |
| 123 | 178) Bc1-g5       |                  22 |           151 |
| 124 | 123) Ke5-f6       |                  22 |           293 |
| 125 | 2) Qf3xf6         |                  22 |           431 |
| 126 | 36) Kd2-c1        |                  22 |           439 |
| 127 | 44) g3-g4         |                  22 |           467 |
| 128 | 79) Bd3xg6        |                  21 |           138 |
| 129 | 114) Ne5xd3       |                  21 |           162 |
| 130 | 24) Rc1xc3        |                  21 |           285 |
| 131 | 87) c7-c8N        |                  21 |           300 |
| 132 | 65) .. Ba6-c8     |                  21 |           409 |
| 133 | 200) Bg3-f4       |                  21 |           413 |
| 134 | 164) .. Bb4xa3(?) |                  21 |           459 |
| 135 | 196) Nc3-d5       |                  21 |           605 |
| 136 | 103) Qa3-h3       |                  20 |           257 |
| 137 | 135) Bd8-c7       |                  20 |           289 |
| 138 | 27) Re3-e8        |                  20 |           306 |
| 139 | 155) Bd3-g6       |                  20 |           407 |
| 140 | 1) Ne7-c6         |                  20 |           559 |
| 141 | 53) Bg5-f4        |                  19 |           101 |
| 142 | 28) Ra4-a2        |                  19 |           178 |
| 143 | 179) .. Rd8xd4    |                  19 |           217 |
| 144 | 34) f5-f6         |                  19 |           389 |
| 145 | 20) a4-a5         |                  19 |           469 |
| 146 | 181) h2-h4        |                  18 |           217 |
| 147 | 125) Ne3-g2       |                  18 |           263 |
| 148 | 83) d4-d5         |                  18 |           369 |
| 149 | 116) Nf4-d3       |                  18 |           383 |
| 150 | 169) Bd3xh7       |                  18 |           396 |
| 151 | 156) f4-f5        |                  18 |           480 |
| 152 | 117) .. Rc5-b5(?) |                  18 |           519 |
| 153 | 15) h2-h4         |                  18 |           549 |
| 154 | 43) Ne5-g6        |                  18 |           608 |
| 155 | 13) .. Nb6-c4     |                  17 |           471 |
| 156 | 176) d5-d6        |                  17 |           475 |
| 157 | 90) Bd6-f8        |                  16 |           216 |
| 158 | 54) Bc2-a4        |                  16 |           241 |
| 159 | 133) Bh5-f3       |                  16 |           396 |
| 160 | 76) .. Rh7xh4     |                  15 |            87 |
| 161 | 101) Kh4-h5       |                  15 |           165 |
| 162 | 73) .. e6-e5      |                  15 |           276 |
| 163 | 105) Ne7-c8       |                  15 |           418 |
| 164 | 158) Na3-b5       |                  15 |           444 |
| 165 | 8) Rd4-d6         |                  15 |           615 |
| 166 | 170) Qf3-f6       |                  15 |           662 |
| 167 | 11) g2-g4         |                  14 |           215 |
| 168 | 138) Qh4-d4       |                  14 |           283 |
| 169 | 97) .. Qh5-f5     |                  14 |           505 |
| 170 | 21) .. Rb8xb3     |                  13 |            35 |
| 171 | 141) Ra3-c3       |                  13 |           111 |
| 172 | 195) .. Rh6xh2    |                  13 |           236 |
| 173 | 209) Bc1-d2       |                  13 |           249 |
| 174 | 19) Ng3-f5        |                  13 |           662 |
| 175 | 108) Be2-h5       |                  12 |           267 |
| 176 | 14) Qf4-f6        |                  12 |           412 |
| 177 | 113) Ng4-f6       |                  12 |           550 |
| 178 | 126) Nd4-c6       |                  12 |           653 |
| 179 | 58) Ng5xf7        |                  11 |           228 |
| 180 | 208) Bd3xh7       |                  11 |           237 |
| 181 | 3) Nb8-c6         |                  11 |           509 |
| 182 | 39) .. Rd6-f6     |                  11 |           563 |
| 183 | 51) b4-b5         |                  10 |           216 |
| 184 | 177) Nf3-h4       |                  10 |           501 |
| 185 | 80) Bh6-g5        |                   9 |            49 |
| 186 | 95) Kg2-f3        |                   9 |           397 |
| 187 | 144) Bg5-f6       |                   9 |           508 |
| 188 | 99) .. Qd3xg3     |                   9 |           730 |
| 189 | 150) Bd4-f6       |                   9 |           967 |
| 190 | 93) Nc6xe7        |                   8 |            53 |
| 191 | 69) Re8xe5        |                   8 |           116 |
| 192 | 89) .. Re2xd2     |                   8 |           282 |
| 193 | 70) a7-a8B        |                   8 |           337 |
| 194 | 130) f2-f4        |                   8 |           364 |
| 195 | 18) Be1-d2        |                   7 |           148 |
| 196 | 153) Ne2-d4       |                   7 |           232 |
| 197 | 131) Na8-c7       |                   7 |           626 |
| 198 | 78) Qd6xe5        |                   7 |           638 |
| 199 | 184) .. Bf5-g4    |                   7 |           884 |
| 200 | 26) Ne2-f4        |                   7 |           936 |
| 201 | 91) Be3xc5        |                   6 |           114 |
| 202 | 204) Bc1-g5       |                   6 |           215 |
| 203 | 67) f3-f4         |                   6 |           322 |
| 204 | 68) Qc7-d8        |                   6 |           379 |
| 205 | 57) Nc2-d4        |                   5 |           193 |
| 206 | 77) Nc4-a5        |                   5 |           382 |
| 207 | 7) Rh4xh1         |                   4 |            54 |
| 208 | 74) Kb7-c8        |                   4 |           324 |
| 209 | 38) Ne4-c3        |                   4 |           524 |
| 210 | 102) h5xg6        |                   3 |           497 |
| 211 | 33) Nf7-d6        |                   2 |           964 |
| 212 | 23) Nf3-h4        |                   0 |           nan |
+-----+-------------------+---------------------+---------------+
```

### D. Credits
* Vinvin from [talkchess](http://talkchess.com/forum3/index.php)

