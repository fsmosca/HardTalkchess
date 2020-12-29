# Hard Talkchess
The epd of this test suite is in the docs/2020 folder. Topic is [discussed in talkchess](http://talkchess.com/forum3/viewtopic.php?f=2&t=72902).

### Setup
In case you need to use the script hard.py, ranking.py and top_hard.py to get the ranking of hard positions, ranking of engines that solves more positions in case the main data `hard_talkchess_2020_table.csv` will be updated, or extract the top 10 hardest epd then install the following libraries.

##### Method 1
* pip install pandas
* pip install tabulate

##### Method 2
* pip install -r requirements.txt

### Command line
* To get hard positions ranking  
`python hard.py` 

* To get ranking of engines  
`python ranking.py`

* To get the top 10 hardest epd  
`python top_hard.py`  
Modify the code to get the top 50  
`num_top = 50`

### A. Engine Ranking

```
+----+----------------------+------------+---------------+-------------+------------------------------+----------------+-----------+
|    | name                 |   numsolve |   meantimesec |   pospermin | cpu                          | gpu            |   threads |
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

### B. Hard Positions Ranking
```
+-----+-------------------+---------------------+---------------+
|     | Solution          |   NumEngSolvedCount |   MeanTimeSec |
|-----+-------------------+---------------------+---------------|
|   0 | 23) Nf3-h4        |                   1 |             0 |
|   1 | 33) Nf7-d6        |                   2 |           964 |
|   2 | 102) h5xg6        |                   3 |           497 |
|   3 | 74) Kb7-c8        |                   4 |           324 |
|   4 | 7) Rh4xh1         |                   4 |            54 |
|   5 | 38) Ne4-c3        |                   5 |           420 |
|   6 | 57) Nc2-d4        |                   5 |           193 |
|   7 | 68) Qc7-d8        |                   6 |           379 |
|   8 | 67) f3-f4         |                   6 |           322 |
|   9 | 77) Nc4-a5        |                   6 |           318 |
|  10 | 204) Bc1-g5       |                   6 |           215 |
|  11 | 91) Be3xc5        |                   6 |           114 |
|  12 | 26) Ne2-f4        |                   7 |           936 |
|  13 | 184) .. Bf5-g4    |                   7 |           884 |
|  14 | 131) Na8-c7       |                   7 |           626 |
|  15 | 153) Ne2-d4       |                   7 |           232 |
|  16 | 78) Qd6xe5        |                   8 |           561 |
|  17 | 130) f2-f4        |                   8 |           364 |
|  18 | 70) a7-a8B        |                   8 |           337 |
|  19 | 18) Be1-d2        |                   8 |           131 |
|  20 | 93) Nc6xe7        |                   8 |            53 |
|  21 | 144) Bg5-f6       |                   9 |           508 |
|  22 | 89) .. Re2xd2     |                   9 |           251 |
|  23 | 69) Re8xe5        |                   9 |           103 |
|  24 | 80) Bh6-g5        |                   9 |            49 |
|  25 | 150) Bd4-f6       |                  10 |           870 |
|  26 | 99) .. Qd3xg3     |                  10 |           657 |
|  27 | 95) Kg2-f3        |                  10 |           357 |
|  28 | 39) .. Rd6-f6     |                  11 |           563 |
|  29 | 3) Nb8-c6         |                  11 |           509 |
|  30 | 177) Nf3-h4       |                  11 |           462 |
|  31 | 51) b4-b5         |                  11 |           196 |
|  32 | 126) Nd4-c6       |                  12 |           653 |
|  33 | 113) Ng4-f6       |                  12 |           550 |
|  34 | 108) Be2-h5       |                  12 |           267 |
|  35 | 208) Bd3xh7       |                  12 |           217 |
|  36 | 58) Ng5xf7        |                  12 |           209 |
|  37 | 19) Ng3-f5        |                  13 |           662 |
|  38 | 14) Qf4-f6        |                  13 |           381 |
|  39 | 195) .. Rh6xh2    |                  13 |           236 |
|  40 | 141) Ra3-c3       |                  13 |           111 |
|  41 | 21) .. Rb8xb3     |                  13 |            35 |
|  42 | 138) Qh4-d4       |                  14 |           283 |
|  43 | 209) Bc1-d2       |                  14 |           231 |
|  44 | 11) g2-g4         |                  14 |           215 |
|  45 | 8) Rd4-d6         |                  15 |           615 |
|  46 | 97) .. Qh5-f5     |                  15 |           472 |
|  47 | 105) Ne7-c8       |                  15 |           418 |
|  48 | 76) .. Rh7xh4     |                  15 |            87 |
|  49 | 170) Qf3-f6       |                  16 |           622 |
|  50 | 158) Na3-b5       |                  16 |           416 |
|  51 | 133) Bh5-f3       |                  16 |           396 |
|  52 | 73) .. e6-e5      |                  16 |           258 |
|  53 | 54) Bc2-a4        |                  16 |           241 |
|  54 | 90) Bd6-f8        |                  16 |           216 |
|  55 | 101) Kh4-h5       |                  16 |           157 |
|  56 | 43) Ne5-g6        |                  18 |           608 |
|  57 | 156) f4-f5        |                  18 |           480 |
|  58 | 176) d5-d6        |                  18 |           449 |
|  59 | 13) .. Nb6-c4     |                  18 |           445 |
|  60 | 169) Bd3xh7       |                  18 |           396 |
|  61 | 83) d4-d5         |                  18 |           369 |
|  62 | 15) h2-h4         |                  19 |           520 |
|  63 | 117) .. Rc5-b5(?) |                  19 |           492 |
|  64 | 34) f5-f6         |                  19 |           389 |
|  65 | 116) Nf4-d3       |                  19 |           363 |
|  66 | 125) Ne3-g2       |                  19 |           254 |
|  67 | 179) .. Rd8xd4    |                  19 |           217 |
|  68 | 181) h2-h4        |                  19 |           205 |
|  69 | 53) Bg5-f4        |                  19 |           101 |
|  70 | 20) a4-a5         |                  20 |           446 |
|  71 | 135) Bd8-c7       |                  20 |           289 |
|  72 | 103) Qa3-h3       |                  20 |           257 |
|  73 | 28) Ra4-a2        |                  20 |           170 |
|  74 | 196) Nc3-d5       |                  21 |           605 |
|  75 | 1) Ne7-c6         |                  21 |           532 |
|  76 | 155) Bd3-g6       |                  21 |           388 |
|  77 | 87) c7-c8N        |                  21 |           300 |
|  78 | 27) Re3-e8        |                  21 |           293 |
|  79 | 24) Rc1xc3        |                  21 |           285 |
|  80 | 36) Kd2-c1        |                  22 |           439 |
|  81 | 164) .. Bb4xa3(?) |                  22 |           439 |
|  82 | 2) Qf3xf6         |                  22 |           431 |
|  83 | 200) Bg3-f4       |                  22 |           394 |
|  84 | 65) .. Ba6-c8     |                  22 |           391 |
|  85 | 123) Ke5-f6       |                  22 |           293 |
|  86 | 114) Ne5xd3       |                  22 |           155 |
|  87 | 79) Bd3xg6        |                  22 |           132 |
|  88 | 59) Ne3-f5        |                  23 |           510 |
|  89 | 44) g3-g4         |                  23 |           447 |
|  90 | 66) .. e5-e4      |                  23 |           302 |
|  91 | 178) Bc1-g5       |                  23 |           144 |
|  92 | 140) Be3-d4       |                  23 |            95 |
|  93 | 182) Ng3-h5       |                  24 |           641 |
|  94 | 192) Qe2xd2, Ne5- |                  24 |           532 |
|  95 | 185) .. Kg8-g7    |                  24 |           274 |
|  96 | 98) .. Re3xf3     |                  24 |           232 |
|  97 | 109) Bc4-e2       |                  24 |           224 |
|  98 | 190) Qe2-h5       |                  25 |           342 |
|  99 | 6) b3-b4          |                  25 |           311 |
| 100 | 47) Rf2-f4        |                  25 |           288 |
| 101 | 118) .. Re7-a7    |                  25 |           237 |
| 102 | 46) Qg3xe5        |                  25 |           167 |
| 103 | 211) Qd1-f3       |                  25 |           166 |
| 104 | 160) Ne4-g5       |                  26 |           393 |
| 105 | 48) Bd3xh7        |                  26 |           271 |
| 106 | 194) .. e4-e3     |                  26 |           219 |
| 107 | 64) Kc3-d4        |                  26 |           184 |
| 108 | 56) Ne5xg6        |                  27 |           511 |
| 109 | 61) .. f4-f3      |                  27 |           454 |
| 110 | 154) Nd4-f3       |                  27 |           454 |
| 111 | 163) Qe2xe8       |                  27 |           312 |
| 112 | 187) Ba4xc6       |                  27 |           270 |
| 113 | 136) Kb5-a6       |                  27 |           248 |
| 114 | 129) Bb4-a5       |                  27 |           198 |
| 115 | 10) Rd6xf6        |                  27 |           164 |
| 116 | 119) h4-h5        |                  28 |           416 |
| 117 | 110) Kf2-e1       |                  28 |           398 |
| 118 | 12) Rg1xg7        |                  28 |           348 |
| 119 | 159) Bd3xh7       |                  28 |           282 |
| 120 | 37) Re1-e6        |                  28 |           261 |
| 121 | 49) Kh2-g3        |                  28 |           215 |
| 122 | 16) Bd3xh7        |                  28 |           208 |
| 123 | 75) Rd7-d2        |                  28 |           197 |
| 124 | 122) .. Bf5-h3    |                  28 |           179 |
| 125 | 104) b7-b8R       |                  28 |           102 |
| 126 | 172) Rd1-d3       |                  28 |            70 |
| 127 | 42) b2-b4         |                  28 |            60 |
| 128 | 165) b6-b7        |                  29 |           603 |
| 129 | 81) Rg2xg7        |                  29 |           481 |
| 130 | 35) Qe3xg5        |                  29 |           414 |
| 131 | 189) Qf3xf4       |                  29 |           384 |
| 132 | 148) Bd3xh7       |                  29 |           304 |
| 133 | 157) Kg1-f2       |                  29 |           298 |
| 134 | 29) e4-e5         |                  29 |           255 |
| 135 | 52) Bd5xf7        |                  29 |           163 |
| 136 | 60) Nh3-g5        |                  29 |           106 |
| 137 | 111) .. e4-e3     |                  29 |            76 |
| 138 | 120) c3-c4        |                  29 |            70 |
| 139 | 88) Qf5-e6        |                  29 |            51 |
| 140 | 85) h5-h6         |                  30 |           275 |
| 141 | 203) g2-g3        |                  30 |           176 |
| 142 | 121) Na5-b3       |                  30 |           152 |
| 143 | 25) e4-e5         |                  30 |           134 |
| 144 | 41) c4-c5         |                  30 |            98 |
| 145 | 149) Bd3xh7       |                  30 |            75 |
| 146 | 127) .. Nb6xc4    |                  31 |           479 |
| 147 | 197) .. Qb2-c2    |                  31 |           420 |
| 148 | 100) a5-a6        |                  31 |           359 |
| 149 | 152) Rd1xd7       |                  31 |           273 |
| 150 | 198) Ne7-d5       |                  31 |           256 |
| 151 | 94) b3-b4         |                  31 |           168 |
| 152 | 5) Qc1-h6         |                  31 |           154 |
| 153 | 22) g2-g4         |                  31 |            82 |
| 154 | 30) Rf1xf6        |                  31 |            57 |
| 155 | 147) Rd1-d8       |                  32 |           485 |
| 156 | 31) Rc8xc7        |                  32 |           318 |
| 157 | 146) Rd1-d8       |                  32 |           286 |
| 158 | 167) Nd5-f6       |                  32 |           258 |
| 159 | 50) Rf1-f5        |                  32 |           250 |
| 160 | 212) Qe3-d3       |                  32 |           200 |
| 161 | 186) Rf3-f6       |                  32 |           199 |
| 162 | 124) Ke2-d3       |                  32 |           190 |
| 163 | 72) g5-g6         |                  32 |           162 |
| 164 | 202) e5-e6        |                  32 |           143 |
| 165 | 55) Qd8-a8        |                  32 |           130 |
| 166 | 84) Rd3xb3        |                  32 |           121 |
| 167 | 171) Qf3-f6       |                  33 |           481 |
| 168 | 62) .. Qg5xg3     |                  33 |           324 |
| 169 | 206) Rf1-f6       |                  33 |           295 |
| 170 | 183) Ne3-g4       |                  33 |           259 |
| 171 | 180) .. O-O-O     |                  33 |           184 |
| 172 | 96) Nc3-d5        |                  33 |           164 |
| 173 | 134) Rh1-h6       |                  33 |           152 |
| 174 | 174) g2-g4        |                  33 |           126 |
| 175 | 151) Bd3xh7       |                  33 |           116 |
| 176 | 115) Rf4-g4       |                  33 |            98 |
| 177 | 112) Rf1-c1       |                  33 |            53 |
| 178 | 132) .. Qe4xc4    |                  34 |           297 |
| 179 | 191) Bd3xh7       |                  34 |           297 |
| 180 | 45) Qc6-f3        |                  34 |           284 |
| 181 | 201) Bd3xh7       |                  34 |           255 |
| 182 | 175) Nd4-c6       |                  34 |           197 |
| 183 | 4) e4-e5          |                  34 |           195 |
| 184 | 142) Bf1-e2       |                  34 |           193 |
| 185 | 106) .. Rd7xd4    |                  34 |           152 |
| 186 | 17) Nf3-g5        |                  34 |           146 |
| 187 | 32) Ng3-h5        |                  34 |           114 |
| 188 | 63) h4-h5         |                  34 |           107 |
| 189 | 82) Ng7-f5        |                  34 |            84 |
| 190 | 107) f4-f5        |                  34 |            84 |
| 191 | 213) Ng5xf7       |                  35 |           523 |
| 192 | 166) Nf8-g6       |                  35 |           376 |
| 193 | 173) Qg5-h6       |                  35 |           191 |
| 194 | 207) .. Ne4-d6    |                  35 |           187 |
| 195 | 137) .. Nf6-h5    |                  35 |           160 |
| 196 | 92) .. Bb7-d5     |                  35 |           115 |
| 197 | 210) Qd1-h5       |                  36 |           305 |
| 198 | 139) .. Ne8-c7    |                  36 |           266 |
| 199 | 199) d5-d6        |                  36 |           244 |
| 200 | 168) Nd5-f6       |                  36 |           201 |
| 201 | 71) .. h7-h5      |                  36 |           159 |
| 202 | 40) Kh3-g2        |                  36 |            93 |
| 203 | 86) c2-c4         |                  36 |            42 |
| 204 | 162) Rh1xh7       |                  36 |            32 |
| 205 | 128) Bb2-a3       |                  36 |            21 |
| 206 | 9) Bd3xh7         |                  36 |            12 |
| 207 | 205) Rd1-g1       |                  37 |           287 |
| 208 | 193) .. c3xb2     |                  37 |           228 |
| 209 | 188) Rd3-h3       |                  37 |           159 |
| 210 | 161) Bd3xh7       |                  37 |            93 |
| 211 | 145) Rd1-d8       |                  37 |            91 |
| 212 | 143) Re1xe7       |                  37 |            55 |
+-----+-------------------+---------------------+---------------+
```

### C. Easy Positions Ranking
```
+-----+-------------------+---------------------+---------------+
|     | Solution          |   NumEngSolvedCount |   MeanTimeSec |
|-----+-------------------+---------------------+---------------|
|   0 | 143) Re1xe7       |                  37 |            55 |
|   1 | 145) Rd1-d8       |                  37 |            91 |
|   2 | 161) Bd3xh7       |                  37 |            93 |
|   3 | 188) Rd3-h3       |                  37 |           159 |
|   4 | 193) .. c3xb2     |                  37 |           228 |
|   5 | 205) Rd1-g1       |                  37 |           287 |
|   6 | 9) Bd3xh7         |                  36 |            12 |
|   7 | 128) Bb2-a3       |                  36 |            21 |
|   8 | 162) Rh1xh7       |                  36 |            32 |
|   9 | 86) c2-c4         |                  36 |            42 |
|  10 | 40) Kh3-g2        |                  36 |            93 |
|  11 | 71) .. h7-h5      |                  36 |           159 |
|  12 | 168) Nd5-f6       |                  36 |           201 |
|  13 | 199) d5-d6        |                  36 |           244 |
|  14 | 139) .. Ne8-c7    |                  36 |           266 |
|  15 | 210) Qd1-h5       |                  36 |           305 |
|  16 | 92) .. Bb7-d5     |                  35 |           115 |
|  17 | 137) .. Nf6-h5    |                  35 |           160 |
|  18 | 207) .. Ne4-d6    |                  35 |           187 |
|  19 | 173) Qg5-h6       |                  35 |           191 |
|  20 | 166) Nf8-g6       |                  35 |           376 |
|  21 | 213) Ng5xf7       |                  35 |           523 |
|  22 | 82) Ng7-f5        |                  34 |            84 |
|  23 | 107) f4-f5        |                  34 |            84 |
|  24 | 63) h4-h5         |                  34 |           107 |
|  25 | 32) Ng3-h5        |                  34 |           114 |
|  26 | 17) Nf3-g5        |                  34 |           146 |
|  27 | 106) .. Rd7xd4    |                  34 |           152 |
|  28 | 142) Bf1-e2       |                  34 |           193 |
|  29 | 4) e4-e5          |                  34 |           195 |
|  30 | 175) Nd4-c6       |                  34 |           197 |
|  31 | 201) Bd3xh7       |                  34 |           255 |
|  32 | 45) Qc6-f3        |                  34 |           284 |
|  33 | 132) .. Qe4xc4    |                  34 |           297 |
|  34 | 191) Bd3xh7       |                  34 |           297 |
|  35 | 112) Rf1-c1       |                  33 |            53 |
|  36 | 115) Rf4-g4       |                  33 |            98 |
|  37 | 151) Bd3xh7       |                  33 |           116 |
|  38 | 174) g2-g4        |                  33 |           126 |
|  39 | 134) Rh1-h6       |                  33 |           152 |
|  40 | 96) Nc3-d5        |                  33 |           164 |
|  41 | 180) .. O-O-O     |                  33 |           184 |
|  42 | 183) Ne3-g4       |                  33 |           259 |
|  43 | 206) Rf1-f6       |                  33 |           295 |
|  44 | 62) .. Qg5xg3     |                  33 |           324 |
|  45 | 171) Qf3-f6       |                  33 |           481 |
|  46 | 84) Rd3xb3        |                  32 |           121 |
|  47 | 55) Qd8-a8        |                  32 |           130 |
|  48 | 202) e5-e6        |                  32 |           143 |
|  49 | 72) g5-g6         |                  32 |           162 |
|  50 | 124) Ke2-d3       |                  32 |           190 |
|  51 | 186) Rf3-f6       |                  32 |           199 |
|  52 | 212) Qe3-d3       |                  32 |           200 |
|  53 | 50) Rf1-f5        |                  32 |           250 |
|  54 | 167) Nd5-f6       |                  32 |           258 |
|  55 | 146) Rd1-d8       |                  32 |           286 |
|  56 | 31) Rc8xc7        |                  32 |           318 |
|  57 | 147) Rd1-d8       |                  32 |           485 |
|  58 | 30) Rf1xf6        |                  31 |            57 |
|  59 | 22) g2-g4         |                  31 |            82 |
|  60 | 5) Qc1-h6         |                  31 |           154 |
|  61 | 94) b3-b4         |                  31 |           168 |
|  62 | 198) Ne7-d5       |                  31 |           256 |
|  63 | 152) Rd1xd7       |                  31 |           273 |
|  64 | 100) a5-a6        |                  31 |           359 |
|  65 | 197) .. Qb2-c2    |                  31 |           420 |
|  66 | 127) .. Nb6xc4    |                  31 |           479 |
|  67 | 149) Bd3xh7       |                  30 |            75 |
|  68 | 41) c4-c5         |                  30 |            98 |
|  69 | 25) e4-e5         |                  30 |           134 |
|  70 | 121) Na5-b3       |                  30 |           152 |
|  71 | 203) g2-g3        |                  30 |           176 |
|  72 | 85) h5-h6         |                  30 |           275 |
|  73 | 88) Qf5-e6        |                  29 |            51 |
|  74 | 120) c3-c4        |                  29 |            70 |
|  75 | 111) .. e4-e3     |                  29 |            76 |
|  76 | 60) Nh3-g5        |                  29 |           106 |
|  77 | 52) Bd5xf7        |                  29 |           163 |
|  78 | 29) e4-e5         |                  29 |           255 |
|  79 | 157) Kg1-f2       |                  29 |           298 |
|  80 | 148) Bd3xh7       |                  29 |           304 |
|  81 | 189) Qf3xf4       |                  29 |           384 |
|  82 | 35) Qe3xg5        |                  29 |           414 |
|  83 | 81) Rg2xg7        |                  29 |           481 |
|  84 | 165) b6-b7        |                  29 |           603 |
|  85 | 42) b2-b4         |                  28 |            60 |
|  86 | 172) Rd1-d3       |                  28 |            70 |
|  87 | 104) b7-b8R       |                  28 |           102 |
|  88 | 122) .. Bf5-h3    |                  28 |           179 |
|  89 | 75) Rd7-d2        |                  28 |           197 |
|  90 | 16) Bd3xh7        |                  28 |           208 |
|  91 | 49) Kh2-g3        |                  28 |           215 |
|  92 | 37) Re1-e6        |                  28 |           261 |
|  93 | 159) Bd3xh7       |                  28 |           282 |
|  94 | 12) Rg1xg7        |                  28 |           348 |
|  95 | 110) Kf2-e1       |                  28 |           398 |
|  96 | 119) h4-h5        |                  28 |           416 |
|  97 | 10) Rd6xf6        |                  27 |           164 |
|  98 | 129) Bb4-a5       |                  27 |           198 |
|  99 | 136) Kb5-a6       |                  27 |           248 |
| 100 | 187) Ba4xc6       |                  27 |           270 |
| 101 | 163) Qe2xe8       |                  27 |           312 |
| 102 | 61) .. f4-f3      |                  27 |           454 |
| 103 | 154) Nd4-f3       |                  27 |           454 |
| 104 | 56) Ne5xg6        |                  27 |           511 |
| 105 | 64) Kc3-d4        |                  26 |           184 |
| 106 | 194) .. e4-e3     |                  26 |           219 |
| 107 | 48) Bd3xh7        |                  26 |           271 |
| 108 | 160) Ne4-g5       |                  26 |           393 |
| 109 | 211) Qd1-f3       |                  25 |           166 |
| 110 | 46) Qg3xe5        |                  25 |           167 |
| 111 | 118) .. Re7-a7    |                  25 |           237 |
| 112 | 47) Rf2-f4        |                  25 |           288 |
| 113 | 6) b3-b4          |                  25 |           311 |
| 114 | 190) Qe2-h5       |                  25 |           342 |
| 115 | 109) Bc4-e2       |                  24 |           224 |
| 116 | 98) .. Re3xf3     |                  24 |           232 |
| 117 | 185) .. Kg8-g7    |                  24 |           274 |
| 118 | 192) Qe2xd2, Ne5- |                  24 |           532 |
| 119 | 182) Ng3-h5       |                  24 |           641 |
| 120 | 140) Be3-d4       |                  23 |            95 |
| 121 | 178) Bc1-g5       |                  23 |           144 |
| 122 | 66) .. e5-e4      |                  23 |           302 |
| 123 | 44) g3-g4         |                  23 |           447 |
| 124 | 59) Ne3-f5        |                  23 |           510 |
| 125 | 79) Bd3xg6        |                  22 |           132 |
| 126 | 114) Ne5xd3       |                  22 |           155 |
| 127 | 123) Ke5-f6       |                  22 |           293 |
| 128 | 65) .. Ba6-c8     |                  22 |           391 |
| 129 | 200) Bg3-f4       |                  22 |           394 |
| 130 | 2) Qf3xf6         |                  22 |           431 |
| 131 | 36) Kd2-c1        |                  22 |           439 |
| 132 | 164) .. Bb4xa3(?) |                  22 |           439 |
| 133 | 24) Rc1xc3        |                  21 |           285 |
| 134 | 27) Re3-e8        |                  21 |           293 |
| 135 | 87) c7-c8N        |                  21 |           300 |
| 136 | 155) Bd3-g6       |                  21 |           388 |
| 137 | 1) Ne7-c6         |                  21 |           532 |
| 138 | 196) Nc3-d5       |                  21 |           605 |
| 139 | 28) Ra4-a2        |                  20 |           170 |
| 140 | 103) Qa3-h3       |                  20 |           257 |
| 141 | 135) Bd8-c7       |                  20 |           289 |
| 142 | 20) a4-a5         |                  20 |           446 |
| 143 | 53) Bg5-f4        |                  19 |           101 |
| 144 | 181) h2-h4        |                  19 |           205 |
| 145 | 179) .. Rd8xd4    |                  19 |           217 |
| 146 | 125) Ne3-g2       |                  19 |           254 |
| 147 | 116) Nf4-d3       |                  19 |           363 |
| 148 | 34) f5-f6         |                  19 |           389 |
| 149 | 117) .. Rc5-b5(?) |                  19 |           492 |
| 150 | 15) h2-h4         |                  19 |           520 |
| 151 | 83) d4-d5         |                  18 |           369 |
| 152 | 169) Bd3xh7       |                  18 |           396 |
| 153 | 13) .. Nb6-c4     |                  18 |           445 |
| 154 | 176) d5-d6        |                  18 |           449 |
| 155 | 156) f4-f5        |                  18 |           480 |
| 156 | 43) Ne5-g6        |                  18 |           608 |
| 157 | 101) Kh4-h5       |                  16 |           157 |
| 158 | 90) Bd6-f8        |                  16 |           216 |
| 159 | 54) Bc2-a4        |                  16 |           241 |
| 160 | 73) .. e6-e5      |                  16 |           258 |
| 161 | 133) Bh5-f3       |                  16 |           396 |
| 162 | 158) Na3-b5       |                  16 |           416 |
| 163 | 170) Qf3-f6       |                  16 |           622 |
| 164 | 76) .. Rh7xh4     |                  15 |            87 |
| 165 | 105) Ne7-c8       |                  15 |           418 |
| 166 | 97) .. Qh5-f5     |                  15 |           472 |
| 167 | 8) Rd4-d6         |                  15 |           615 |
| 168 | 11) g2-g4         |                  14 |           215 |
| 169 | 209) Bc1-d2       |                  14 |           231 |
| 170 | 138) Qh4-d4       |                  14 |           283 |
| 171 | 21) .. Rb8xb3     |                  13 |            35 |
| 172 | 141) Ra3-c3       |                  13 |           111 |
| 173 | 195) .. Rh6xh2    |                  13 |           236 |
| 174 | 14) Qf4-f6        |                  13 |           381 |
| 175 | 19) Ng3-f5        |                  13 |           662 |
| 176 | 58) Ng5xf7        |                  12 |           209 |
| 177 | 208) Bd3xh7       |                  12 |           217 |
| 178 | 108) Be2-h5       |                  12 |           267 |
| 179 | 113) Ng4-f6       |                  12 |           550 |
| 180 | 126) Nd4-c6       |                  12 |           653 |
| 181 | 51) b4-b5         |                  11 |           196 |
| 182 | 177) Nf3-h4       |                  11 |           462 |
| 183 | 3) Nb8-c6         |                  11 |           509 |
| 184 | 39) .. Rd6-f6     |                  11 |           563 |
| 185 | 95) Kg2-f3        |                  10 |           357 |
| 186 | 99) .. Qd3xg3     |                  10 |           657 |
| 187 | 150) Bd4-f6       |                  10 |           870 |
| 188 | 80) Bh6-g5        |                   9 |            49 |
| 189 | 69) Re8xe5        |                   9 |           103 |
| 190 | 89) .. Re2xd2     |                   9 |           251 |
| 191 | 144) Bg5-f6       |                   9 |           508 |
| 192 | 93) Nc6xe7        |                   8 |            53 |
| 193 | 18) Be1-d2        |                   8 |           131 |
| 194 | 70) a7-a8B        |                   8 |           337 |
| 195 | 130) f2-f4        |                   8 |           364 |
| 196 | 78) Qd6xe5        |                   8 |           561 |
| 197 | 153) Ne2-d4       |                   7 |           232 |
| 198 | 131) Na8-c7       |                   7 |           626 |
| 199 | 184) .. Bf5-g4    |                   7 |           884 |
| 200 | 26) Ne2-f4        |                   7 |           936 |
| 201 | 91) Be3xc5        |                   6 |           114 |
| 202 | 204) Bc1-g5       |                   6 |           215 |
| 203 | 77) Nc4-a5        |                   6 |           318 |
| 204 | 67) f3-f4         |                   6 |           322 |
| 205 | 68) Qc7-d8        |                   6 |           379 |
| 206 | 57) Nc2-d4        |                   5 |           193 |
| 207 | 38) Ne4-c3        |                   5 |           420 |
| 208 | 7) Rh4xh1         |                   4 |            54 |
| 209 | 74) Kb7-c8        |                   4 |           324 |
| 210 | 102) h5xg6        |                   3 |           497 |
| 211 | 33) Nf7-d6        |                   2 |           964 |
| 212 | 23) Nf3-h4        |                   1 |             0 |
+-----+-------------------+---------------------+---------------+
```

### D. Credits
* Vinvin from [talkchess](http://talkchess.com/forum3/index.php)

