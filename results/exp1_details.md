# Опыт 1: разбор по токенам

## Текст 1

**en** — `Artificial intelligence is changing the way people work and learn.`

- r50k_base (12): [Art] [ificial] [ intelligence] [ is] [ changing] [ the] [ way] [ people] [ work] [ and] [ learn] [.]
- cl100k_base (12): [Art] [ificial] [ intelligence] [ is] [ changing] [ the] [ way] [ people] [ work] [ and] [ learn] [.]
- o200k_base (11): [Artificial] [ intelligence] [ is] [ changing] [ the] [ way] [ people] [ work] [ and] [ learn] [.]

**ru** — `Искусственный интеллект меняет то, как люди работают и учатся.`

- r50k_base (68): [\xd0] [\x98] [с] [к] [у] [с] [с] [т] [в] [е] [н] [н] [ы] [\xd0] [\xb9] [\x20\xd0] [\xb8] [н] [т] [е] [л] [л] [е] [к] [т] [\x20\xd0] [\xbc] [е] [н] [я] [е] [т] [ ] [т] [о] [,] [\x20\xd0] [\xba] [а] [к] [\x20\xd0] [\xbb] [\xd1] [\x8e] [д] [и] [ ] [р] [а] [\xd0] [\xb1] [о] [т] [а] [\xd1] [\x8e] [т] [\x20\xd0] [\xb8] [ ] [у] [\xd1] [\x87] [а] [т] [с] [я] [.]
- cl100k_base (30): [И] [с] [ку] [с] [ств] [ен] [ный] [ ин] [т] [ел] [л] [ект] [ мен] [я] [ет] [ то] [,] [ как] [ лю] [д] [и] [ работ] [а] [ют] [ и] [ у] [ч] [ат] [ся] [.]
- o200k_base (16): [И] [ск] [ус] [ственный] [ интеллект] [ меня] [ет] [ то] [,] [ как] [ люди] [ работают] [ и] [ уч] [атся] [.]

**ru-lat** — `Iskusstvennyj intellekt menyaet to, kak lyudi rabotayut i uchatsya.`

- r50k_base (28): [Is] [kus] [st] [ven] [ny] [j] [ int] [elle] [kt] [ men] [ya] [et] [ to] [,] [ k] [ak] [ ly] [udi] [ rab] [ot] [ay] [ut] [ i] [ u] [ch] [ats] [ya] [.]
- cl100k_base (27): [Is] [kus] [st] [ven] [ny] [j] [ int] [elle] [kt] [ men] [ya] [et] [ to] [,] [ kak] [ ly] [udi] [ rab] [ot] [ay] [ut] [ i] [ u] [ch] [ats] [ya] [.]
- o200k_base (26): [Is] [kus] [st] [ven] [ny] [j] [ int] [elle] [kt] [ men] [ya] [et] [ to] [,] [ kak] [ ly] [udi] [ rab] [ot] [ay] [ut] [ i] [ uch] [ats] [ya] [.]

**kk** — `Жасанды интеллект адамдардың жұмыс істеу және оқу тәсілін өзгертуде.`

- r50k_base (80): [\xd0] [\x96] [а] [с] [а] [н] [д] [ы] [\x20\xd0] [\xb8] [н] [т] [е] [л] [л] [е] [к] [т] [\x20\xd0] [\xb0] [д] [а] [м] [д] [а] [р] [д] [ы] [\xd2] [\xa3] [\x20\xd0] [\xb6] [\xd2] [\xb1] [м] [ы] [с] [ ] [\xd1] [\x96] [с] [т] [е] [у] [\x20\xd0] [\xb6] [\xd3] [\x99] [н] [е] [\x20\xd0] [\xbe] [\xd2] [\x9b] [у] [ ] [т] [\xd3] [\x99] [с] [\xd1] [\x96] [л] [\xd1] [\x96] [н] [ ] [\xd3] [\xa9] [\xd0] [\xb7] [\xd0] [\xb3] [е] [р] [т] [у] [д] [е] [.]
- cl100k_base (55): [\xd0] [\x96] [ас] [анд] [ы] [ ин] [т] [ел] [л] [ект] [ а] [д] [ам] [д] [ар] [д] [ы] [\xd2] [\xa3] [ ж] [\xd2] [\xb1] [м] [ы] [с] [ і] [ст] [е] [у] [ ж] [\xd3] [\x99] [не] [ о] [\xd2] [\x9b] [у] [ т] [\xd3] [\x99] [с] [і] [л] [і] [н] [ ] [\xd3] [\xa9] [з] [г] [ер] [т] [уд] [е] [.]
- o200k_base (19): [Ж] [ас] [анды] [ интеллект] [ адамдар] [дың] [ жұмыс] [ і] [сте] [у] [ және] [ оқу] [ тәс] [іл] [ін] [ өзг] [ерт] [уде] [.]

**kk-lat** — `Jasandy ıntellekt adamdardyń jumys isteý jáne oqý tásilin ózgertýde.`

- r50k_base (40): [J] [as] [andy] [ ] [ı] [nt] [elle] [kt] [ adam] [d] [ardy] [\xc5] [\x84] [ j] [um] [ys] [ is] [te] [\xc3] [\xbd] [ j] [á] [ne] [ o] [q] [\xc3] [\xbd] [ t] [á] [sil] [in] [\x20\xc3] [\xb3] [z] [g] [ert] [\xc3] [\xbd] [de] [.]
- cl100k_base (34): [J] [as] [andy] [ ] [ı] [nt] [elle] [kt] [ adam] [d] [ardy] [ń] [ j] [um] [ys] [ ist] [e] [ý] [ já] [ne] [ o] [q] [ý] [ t] [ás] [il] [in] [ ó] [z] [g] [ert] [ý] [de] [.]
- o200k_base (28): [J] [as] [andy] [ ] [ınt] [elle] [kt] [ adam] [d] [ardy] [ń] [ jum] [ys] [ iste] [ý] [ já] [ne] [ oq] [ý] [ t] [ás] [ilin] [ ó] [zg] [ert] [ý] [de] [.]

## Текст 2

**en** — `Good morning! How are you today? I hope you have a wonderful day.`

- r50k_base (16): [Good] [ morning] [!] [ How] [ are] [ you] [ today] [?] [ I] [ hope] [ you] [ have] [ a] [ wonderful] [ day] [.]
- cl100k_base (16): [Good] [ morning] [!] [ How] [ are] [ you] [ today] [?] [ I] [ hope] [ you] [ have] [ a] [ wonderful] [ day] [.]
- o200k_base (16): [Good] [ morning] [!] [ How] [ are] [ you] [ today] [?] [ I] [ hope] [ you] [ have] [ a] [ wonderful] [ day] [.]

**ru** — `Доброе утро! Как у вас дела сегодня? Надеюсь, у вас будет замечательный день.`

- r50k_base (82): [\xd0] [\x94] [\xd0\xbe\xd0] [\xb1] [р] [о] [е] [ ] [у] [т] [р] [о] [!] [\x20\xd0] [\x9a] [а] [к] [ ] [у] [\x20\xd0] [\xb2] [а] [с] [\x20\xd0] [\xb4] [е] [л] [а] [ ] [с] [е] [\xd0] [\xb3] [\xd0\xbe\xd0] [\xb4] [н] [я] [?] [\x20\xd0] [\x9d] [а] [д] [е] [\xd1] [\x8e] [с] [ь] [,] [ ] [у] [\x20\xd0] [\xb2] [а] [с] [\x20\xd0] [\xb1] [у] [д] [е] [т] [\x20\xd0] [\xb7] [а] [м] [е] [\xd1] [\x87] [а] [т] [е] [л] [ь] [н] [ы] [\xd0] [\xb9] [\x20\xd0] [\xb4] [е] [н] [ь] [.]
- cl100k_base (40): [Д] [об] [р] [ое] [ у] [т] [р] [о] [!] [ К] [ак] [ у] [ в] [ас] [ дел] [а] [ с] [ег] [од] [ня] [?] [ Н] [ад] [е] [ю] [с] [ь] [,] [ у] [ в] [ас] [ будет] [ з] [ам] [еч] [атель] [ный] [ д] [ень] [.]
- o200k_base (23): [Доб] [ро] [е] [ ут] [ро] [!] [ Как] [ у] [ вас] [ дела] [ сегодня] [?] [ Над] [е] [юсь] [,] [ у] [ вас] [ будет] [ замеч] [ательный] [ день] [.]

**ru-lat** — `Dobroe utro! Kak u vas dela segodnya? Nadeyus, u vas budet zamechatelnyj den.`

- r50k_base (33): [D] [ob] [roe] [ ut] [ro] [!] [ Kak] [ u] [ vas] [ del] [a] [ se] [god] [ny] [a] [?] [ N] [ade] [y] [us] [,] [ u] [ vas] [ bud] [et] [ z] [ame] [ch] [atel] [ny] [j] [ den] [.]
- cl100k_base (31): [D] [ob] [roe] [ ut] [ro] [!] [ Kak] [ u] [ vas] [ dela] [ seg] [od] [nya] [?] [ N] [ade] [y] [us] [,] [ u] [ vas] [ bud] [et] [ z] [ame] [chat] [el] [ny] [j] [ den] [.]
- o200k_base (29): [Dob] [roe] [ ut] [ro] [!] [ Kak] [ u] [ vas] [ dela] [ seg] [od] [nya] [?] [ Nad] [ey] [us] [,] [ u] [ vas] [ bud] [et] [ z] [ame] [chat] [el] [ny] [j] [ den] [.]

**kk** — `Қайырлы таң! Бүгін жағдайыңыз қалай? Күніңіз керемет өтеді деп үміттенемін.`

- r50k_base (98): [\xd2] [\x9a] [а] [\xd0] [\xb9] [ы] [р] [л] [ы] [ ] [т] [а] [\xd2] [\xa3] [!] [\x20\xd0] [\x91] [\xd2] [\xaf] [\xd0] [\xb3] [\xd1] [\x96] [н] [\x20\xd0] [\xb6] [а] [\xd2] [\x93] [д] [а] [\xd0] [\xb9] [ы] [\xd2] [\xa3] [ы] [\xd0] [\xb7] [ ] [\xd2] [\x9b] [а] [л] [а] [\xd0] [\xb9] [?] [\x20\xd0] [\x9a] [\xd2] [\xaf] [н] [\xd1] [\x96] [\xd2] [\xa3] [\xd1] [\x96] [\xd0] [\xb7] [\x20\xd0] [\xba] [е] [р] [е] [м] [е] [т] [ ] [\xd3] [\xa9] [т] [е] [д] [\xd1] [\x96] [\x20\xd0] [\xb4] [е] [\xd0] [\xbf] [ ] [\xd2] [\xaf] [м] [\xd1] [\x96] [т] [т] [е] [н] [е] [м] [\xd1] [\x96] [н] [.]
- cl100k_base (68): [\xd2] [\x9a] [ай] [ы] [р] [л] [ы] [ т] [а] [\xd2] [\xa3] [!] [ Б] [\xd2] [\xaf] [г] [і] [н] [ ж] [а] [\xd2] [\x93] [д] [ай] [ы] [\xd2] [\xa3] [ы] [з] [ ] [\xd2] [\x9b] [ал] [ай] [?] [ К] [\xd2] [\xaf] [н] [і] [\xd2] [\xa3] [і] [з] [ к] [ер] [ем] [ет] [ ] [\xd3] [\xa9] [т] [ед] [і] [ д] [еп] [ ] [\xd2] [\xaf] [м] [і] [т] [т] [ен] [ем] [і] [н] [.]
- o200k_base (31): [Қ] [ай] [ыр] [лы] [ таң] [!] [ Б] [үг] [ін] [ жағдай] [ы] [ңыз] [ қалай] [?] [ К] [ү] [нің] [із] [ кер] [ем] [ет] [ өт] [еді] [ деп] [ ү] [мі] [т] [тен] [ем] [ін] [.]

**kk-lat** — `Qaıyrly tań! Búgin jaǵdaıyńyz qalaı? Kúnińiz keremet ótedi dep úmittenemin.`

- r50k_base (45): [Q] [a] [ı] [yr] [ly] [ ta] [\xc5] [\x84] [!] [ B] [ú] [gin] [ ja] [\xc7] [\xb5] [da] [ı] [y] [\xc5] [\x84] [yz] [ q] [ala] [ı] [?] [ K] [ú] [ni] [\xc5] [\x84] [iz] [ ke] [rem] [et] [\x20\xc3] [\xb3] [ted] [i] [ dep] [\x20\xc3] [\xba] [m] [itten] [emin] [.]
- cl100k_base (39): [Q] [a] [ı] [yr] [ly] [ ta] [ń] [!] [ B] [ú] [gin] [ ja] [\xc7] [\xb5] [da] [ı] [y] [ń] [yz] [ q] [ala] [ı] [?] [ K] [ú] [ni] [ń] [iz] [ ker] [emet] [ ó] [ted] [i] [ dep] [ ú] [m] [itten] [emin] [.]
- o200k_base (35): [Qa] [ı] [yr] [ly] [ ta] [ń] [!] [ B] [ú] [gin] [ ja] [\xc7] [\xb5] [da] [ıy] [ń] [yz] [ qala] [ı] [?] [ K] [ú] [ni] [ń] [iz] [ ker] [emet] [ ót] [edi] [ dep] [ ú] [mit] [ten] [emin] [.]

## Текст 3

**en** — `The city council approved a new budget for public transport, which will allow buying fifty electric buses next year.`

- r50k_base (21): [The] [ city] [ council] [ approved] [ a] [ new] [ budget] [ for] [ public] [ transport] [,] [ which] [ will] [ allow] [ buying] [ fifty] [ electric] [ buses] [ next] [ year] [.]
- cl100k_base (21): [The] [ city] [ council] [ approved] [ a] [ new] [ budget] [ for] [ public] [ transport] [,] [ which] [ will] [ allow] [ buying] [ fifty] [ electric] [ buses] [ next] [ year] [.]
- o200k_base (21): [The] [ city] [ council] [ approved] [ a] [ new] [ budget] [ for] [ public] [ transport] [,] [ which] [ will] [ allow] [ buying] [ fifty] [ electric] [ buses] [ next] [ year] [.]

**ru** — `Городской совет утвердил новый бюджет на общественный транспорт, что позволит в следующем году купить пятьдесят электробусов.`

- r50k_base (138): [\xd0] [\x93] [о] [р] [\xd0\xbe\xd0] [\xb4] [с] [к] [\xd0\xbe\xd0] [\xb9] [ ] [с] [\xd0\xbe\xd0] [\xb2] [е] [т] [ ] [у] [т] [в] [е] [р] [д] [и] [л] [\x20\xd0] [\xbd] [\xd0\xbe\xd0] [\xb2] [ы] [\xd0] [\xb9] [\x20\xd0] [\xb1] [\xd1] [\x8e] [д] [\xd0] [\xb6] [е] [т] [\x20\xd0] [\xbd] [а] [\x20\xd0] [\xbe] [\xd0] [\xb1] [\xd1] [\x89] [е] [с] [т] [в] [е] [н] [н] [ы] [\xd0] [\xb9] [ ] [т] [р] [а] [н] [с] [\xd0] [\xbf] [о] [р] [т] [,] [ ] [\xd1] [\x87] [т] [о] [\x20\xd0] [\xbf] [\xd0\xbe\xd0] [\xb7] [в] [\xd0\xbe\xd0] [\xbb] [и] [т] [\x20\xd0] [\xb2] [ ] [с] [л] [е] [д] [у] [\xd1] [\x8e] [\xd1] [\x89] [е] [м] [\x20\xd0] [\xb3] [\xd0\xbe\xd0] [\xb4] [у] [\x20\xd0] [\xba] [у] [\xd0] [\xbf] [и] [т] [ь] [\x20\xd0] [\xbf] [я] [т] [ь] [д] [е] [с] [я] [т] [ ] [\xd1] [\x8d] [л] [е] [к] [т] [р] [\xd0\xbe\xd0] [\xb1] [у] [с] [\xd0\xbe\xd0] [\xb2] [.]
- cl100k_base (60): [Г] [ор] [од] [ск] [ой] [ с] [ов] [ет] [ у] [т] [вер] [д] [ил] [ нов] [ый] [ б] [ю] [д] [ж] [ет] [ на] [ об] [щ] [еств] [ен] [ный] [ т] [ран] [сп] [ор] [т] [,] [ что] [ п] [озв] [ол] [ит] [ в] [ след] [ующ] [ем] [ г] [од] [у] [ к] [уп] [ить] [ п] [ять] [де] [ся] [т] [ э] [л] [ект] [р] [об] [ус] [ов] [.]
- o200k_base (28): [Г] [ород] [ской] [ совет] [ ут] [верд] [ил] [ новый] [ бюджет] [ на] [ обще] [ственный] [ транспорт] [,] [ что] [ позволит] [ в] [ следующ] [ем] [ году] [ купить] [ пять] [де] [сят] [ элект] [роб] [усов] [.]

**ru-lat** — `Gorodskoj sovet utverdil novyj byudzhet na obshchestvennyj transport, chto pozvolit v sleduyushchem godu kupit pyatdesyat elektrobusov.`

- r50k_base (54): [G] [or] [ods] [ko] [j] [ so] [vet] [ ut] [ver] [d] [il] [ no] [vy] [j] [ by] [ud] [z] [het] [ na] [ ob] [sh] [chest] [ven] [ny] [j] [ transport] [,] [ ch] [to] [ po] [z] [v] [olit] [ v] [ sled] [uy] [ush] [chem] [ god] [u] [ k] [up] [it] [ py] [at] [des] [y] [at] [ ele] [kt] [ro] [bus] [ov] [.]
- cl100k_base (52): [G] [or] [od] [sk] [oj] [ so] [vet] [ ut] [ver] [d] [il] [ nov] [y] [j] [ by] [ud] [z] [het] [ na] [ ob] [sh] [chest] [ven] [ny] [j] [ transport] [,] [ c] [ht] [o] [ poz] [vol] [it] [ v] [ sled] [uy] [ush] [chem] [ god] [u] [ kup] [it] [ py] [at] [des] [yat] [ ele] [kt] [ro] [bus] [ov] [.]
- o200k_base (47): [G] [or] [ods] [koj] [ sov] [et] [ ut] [verd] [il] [ nov] [yj] [ by] [udz] [het] [ na] [ ob] [sh] [ch] [est] [ven] [ny] [j] [ transport] [,] [ c] [hto] [ poz] [vol] [it] [ v] [ sle] [du] [y] [ush] [chem] [ god] [u] [ kup] [it] [ py] [at] [des] [yat] [ elektro] [bus] [ov] [.]

**kk** — `Қалалық кеңес қоғамдық көлікке арналған жаңа бюджетті бекітті, бұл келесі жылы елу электр автобусын сатып алуға мүмкіндік береді.`

- r50k_base (153): [\xd2] [\x9a] [а] [л] [а] [л] [ы] [\xd2] [\x9b] [\x20\xd0] [\xba] [е] [\xd2] [\xa3] [е] [с] [ ] [\xd2] [\x9b] [о] [\xd2] [\x93] [а] [м] [д] [ы] [\xd2] [\x9b] [\x20\xd0] [\xba] [\xd3] [\xa9] [л] [\xd1] [\x96] [к] [к] [е] [\x20\xd0] [\xb0] [р] [н] [а] [л] [\xd2] [\x93] [а] [н] [\x20\xd0] [\xb6] [а] [\xd2] [\xa3] [а] [\x20\xd0] [\xb1] [\xd1] [\x8e] [д] [\xd0] [\xb6] [е] [т] [т] [\xd1] [\x96] [\x20\xd0] [\xb1] [е] [к] [\xd1] [\x96] [т] [т] [\xd1] [\x96] [,] [\x20\xd0] [\xb1] [\xd2] [\xb1] [л] [\x20\xd0] [\xba] [е] [л] [е] [с] [\xd1] [\x96] [\x20\xd0] [\xb6] [ы] [л] [ы] [\x20\xd0] [\xb5] [л] [у] [ ] [\xd1] [\x8d] [л] [е] [к] [т] [р] [\x20\xd0] [\xb0] [в] [т] [\xd0\xbe\xd0] [\xb1] [у] [с] [ы] [н] [ ] [с] [а] [т] [ы] [\xd0] [\xbf] [\x20\xd0] [\xb0] [л] [у] [\xd2] [\x93] [а] [\x20\xd0] [\xbc] [\xd2] [\xaf] [м] [к] [\xd1] [\x96] [н] [д] [\xd1] [\x96] [к] [\x20\xd0] [\xb1] [е] [р] [е] [д] [\xd1] [\x96] [.]
- cl100k_base (106): [\xd2] [\x9a] [ал] [ал] [ы] [\xd2] [\x9b] [ к] [е] [\xd2] [\xa3] [ес] [ ] [\xd2] [\x9b] [о] [\xd2] [\x93] [ам] [д] [ы] [\xd2] [\x9b] [ к] [\xd3] [\xa9] [л] [і] [к] [ке] [ а] [р] [на] [л] [\xd2] [\x93] [ан] [ ж] [а] [\xd2] [\xa3] [а] [ б] [ю] [д] [ж] [ет] [т] [і] [ б] [ек] [і] [т] [т] [і] [,] [ б] [\xd2] [\xb1] [л] [ к] [ел] [ес] [і] [ ж] [ы] [л] [ы] [ е] [л] [у] [ э] [л] [ект] [р] [ ав] [т] [об] [ус] [ы] [н] [ с] [ат] [ы] [п] [ а] [л] [у] [\xd2] [\x93] [а] [ м] [\xd2] [\xaf] [м] [к] [і] [н] [д] [і] [к] [ б] [ер] [ед] [і] [.]
- o200k_base (32): [Қ] [ал] [алық] [ кең] [ес] [ қоғамдық] [ кө] [лік] [ке] [ арналған] [ жаңа] [ бюдж] [етті] [ бек] [іт] [ті] [,] [ бұл] [ кел] [есі] [ жылы] [ е] [лу] [ электр] [ автобус] [ын] [ сатып] [ ал] [уға] [ мүмкіндік] [ береді] [.]

**kk-lat** — `Qalalyq keńes qoǵamdyq kólikke arnalǵan jańa bıýdjetti bekitti, bul kelesi jyly elý elektr avtobýsyn satyp alýǵa múmkindik beredi.`

- r50k_base (75): [Q] [al] [aly] [q] [ ke] [\xc5] [\x84] [es] [ q] [o] [\xc7] [\xb5] [am] [dy] [q] [ k] [ó] [lik] [ke] [ ar] [n] [al] [\xc7] [\xb5] [an] [ ja] [\xc5] [\x84] [a] [ b] [ı] [\xc3] [\xbd] [dj] [etti] [ be] [k] [itt] [i] [,] [ bul] [ ke] [lesi] [ j] [y] [ly] [ el] [\xc3] [\xbd] [ ele] [k] [tr] [ av] [t] [ob] [\xc3] [\xbd] [syn] [ sat] [yp] [ al] [\xc3] [\xbd] [\xc7] [\xb5] [a] [ m] [ú] [m] [kind] [ik] [ be] [red] [i] [.]
- cl100k_base (63): [Q] [al] [aly] [q] [ ke] [ń] [es] [ q] [o] [\xc7] [\xb5] [am] [dy] [q] [ k] [ó] [lik] [ke] [ ar] [nal] [\xc7] [\xb5] [an] [ ja] [ń] [a] [ b] [ı] [ý] [dj] [etti] [ bek] [itti] [,] [ bul] [ ke] [lesi] [ j] [y] [ly] [ el] [ý] [ elek] [tr] [ av] [t] [ob] [ý] [syn] [ sat] [yp] [ al] [ý] [\xc7] [\xb5] [a] [ mú] [m] [kind] [ik] [ ber] [edi] [.]
- o200k_base (61): [Q] [al] [aly] [q] [ ke] [ń] [es] [ qo] [\xc7] [\xb5] [am] [dy] [q] [ k] [ó] [lik] [ke] [ ar] [nal] [\xc7] [\xb5] [an] [ ja] [ń] [a] [ b] [ı] [ý] [d] [jet] [ti] [ bek] [itti] [,] [ bul] [ k] [eles] [i] [ jy] [ly] [ el] [ý] [ elektr] [ avt] [ob] [ý] [syn] [ sat] [yp] [ al] [ý] [\xc7] [\xb5] [a] [ mú] [m] [kind] [ik] [ ber] [edi] [.]

## Текст 4

**en** — `A neural network learns by adjusting its weights to reduce the error between its prediction and the correct answer.`

- r50k_base (20): [A] [ neural] [ network] [ learns] [ by] [ adjusting] [ its] [ weights] [ to] [ reduce] [ the] [ error] [ between] [ its] [ prediction] [ and] [ the] [ correct] [ answer] [.]
- cl100k_base (20): [A] [ neural] [ network] [ learns] [ by] [ adjusting] [ its] [ weights] [ to] [ reduce] [ the] [ error] [ between] [ its] [ prediction] [ and] [ the] [ correct] [ answer] [.]
- o200k_base (20): [A] [ neural] [ network] [ learns] [ by] [ adjusting] [ its] [ weights] [ to] [ reduce] [ the] [ error] [ between] [ its] [ prediction] [ and] [ the] [ correct] [ answer] [.]

**ru** — `Нейронная сеть обучается, подбирая свои веса так, чтобы уменьшить ошибку между предсказанием и правильным ответом.`

- r50k_base (125): [\xd0] [\x9d] [е] [\xd0] [\xb9] [р] [о] [н] [н] [а] [я] [ ] [с] [е] [т] [ь] [\x20\xd0] [\xbe] [\xd0] [\xb1] [у] [\xd1] [\x87] [а] [е] [т] [с] [я] [,] [\x20\xd0] [\xbf] [\xd0\xbe\xd0] [\xb4] [\xd0] [\xb1] [и] [р] [а] [я] [ ] [с] [в] [о] [и] [\x20\xd0] [\xb2] [е] [с] [а] [ ] [т] [а] [к] [,] [ ] [\xd1] [\x87] [т] [\xd0\xbe\xd0] [\xb1] [ы] [ ] [у] [м] [е] [н] [ь] [\xd1] [\x88] [и] [т] [ь] [\x20\xd0] [\xbe] [\xd1] [\x88] [и] [\xd0] [\xb1] [к] [у] [\x20\xd0] [\xbc] [е] [\xd0] [\xb6] [д] [у] [\x20\xd0] [\xbf] [р] [е] [д] [с] [к] [а] [\xd0] [\xb7] [а] [н] [и] [е] [м] [\x20\xd0] [\xb8] [\x20\xd0] [\xbf] [р] [а] [в] [и] [л] [ь] [н] [ы] [м] [\x20\xd0] [\xbe] [т] [в] [е] [т] [\xd0\xbe\xd0] [\xbc] [.]
- cl100k_base (50): [Н] [ей] [р] [он] [ная] [ с] [ет] [ь] [ об] [уч] [ается] [,] [ под] [б] [и] [ра] [я] [ св] [о] [и] [ в] [ес] [а] [ так] [,] [ чтобы] [ у] [мен] [ь] [ш] [ить] [ ошиб] [ку] [ м] [еж] [д] [у] [ пред] [с] [каз] [ани] [ем] [ и] [ прав] [иль] [ны] [м] [ ответ] [ом] [.]
- o200k_base (31): [Н] [ей] [рон] [ная] [ сеть] [ обуч] [ается] [,] [ под] [бира] [я] [ свои] [ веса] [ так] [,] [ чтобы] [ уменьш] [ить] [ ошиб] [ку] [ между] [ пред] [с] [каз] [анием] [ и] [ правиль] [ным] [ ответ] [ом] [.]

**ru-lat** — `Nejronnaya set obuchaetsya, podbiraya svoi vesa tak, chtoby umenshit oshibku mezhdu predskazaniem i pravilnym otvetom.`

- r50k_base (50): [Ne] [j] [ron] [n] [aya] [ set] [ ob] [ucha] [ets] [ya] [,] [ pod] [b] [ir] [aya] [ s] [vo] [i] [ v] [esa] [ t] [ak] [,] [ ch] [t] [oby] [ um] [ens] [hit] [ o] [sh] [ib] [ku] [ me] [zh] [du] [ pred] [sk] [az] [ani] [em] [ i] [ pra] [vil] [ny] [m] [ ot] [vet] [om] [.]
- cl100k_base (46): [Ne] [j] [ron] [n] [aya] [ set] [ ob] [ucha] [ets] [ya] [,] [ pod] [bir] [aya] [ svo] [i] [ v] [esa] [ tak] [,] [ c] [ht] [oby] [ um] [ens] [hit] [ o] [sh] [ib] [ku] [ me] [zh] [du] [ pred] [sk] [az] [aniem] [ i] [ pr] [av] [il] [nym] [ ot] [vet] [om] [.]
- o200k_base (42): [Ne] [j] [ron] [n] [aya] [ set] [ ob] [ucha] [ets] [ya] [,] [ pod] [bir] [aya] [ svo] [i] [ v] [esa] [ tak] [,] [ cht] [oby] [ um] [ens] [hit] [ osh] [ib] [ku] [ me] [zh] [du] [ pred] [sk] [az] [aniem] [ i] [ pravil] [nym] [ ot] [vet] [om] [.]

**kk** — `Нейрондық желі болжам мен дұрыс жауап арасындағы қатені азайту үшін өз салмақтарын түзету арқылы оқиды.`

- r50k_base (125): [\xd0] [\x9d] [е] [\xd0] [\xb9] [р] [о] [н] [д] [ы] [\xd2] [\x9b] [\x20\xd0] [\xb6] [е] [л] [\xd1] [\x96] [\x20\xd0] [\xb1] [\xd0\xbe\xd0] [\xbb] [\xd0] [\xb6] [а] [м] [\x20\xd0] [\xbc] [е] [н] [\x20\xd0] [\xb4] [\xd2] [\xb1] [р] [ы] [с] [\x20\xd0] [\xb6] [а] [у] [а] [\xd0] [\xbf] [\x20\xd0] [\xb0] [р] [а] [с] [ы] [н] [д] [а] [\xd2] [\x93] [ы] [ ] [\xd2] [\x9b] [а] [т] [е] [н] [\xd1] [\x96] [\x20\xd0] [\xb0] [\xd0] [\xb7] [а] [\xd0] [\xb9] [т] [у] [ ] [\xd2] [\xaf] [\xd1] [\x88] [\xd1] [\x96] [н] [ ] [\xd3] [\xa9] [\xd0] [\xb7] [ ] [с] [а] [л] [м] [а] [\xd2] [\x9b] [т] [а] [р] [ы] [н] [ ] [т] [\xd2] [\xaf] [\xd0] [\xb7] [е] [т] [у] [\x20\xd0] [\xb0] [р] [\xd2] [\x9b] [ы] [л] [ы] [\x20\xd0] [\xbe] [\xd2] [\x9b] [и] [д] [ы] [.]
- cl100k_base (81): [Н] [ей] [р] [он] [д] [ы] [\xd2] [\x9b] [ ж] [ел] [і] [ б] [олж] [ам] [ мен] [ д] [\xd2] [\xb1] [ры] [с] [ ж] [а] [у] [ап] [ а] [р] [ас] [ы] [н] [да] [\xd2] [\x93] [ы] [ ] [\xd2] [\x9b] [ат] [ен] [і] [ а] [з] [ай] [ту] [ ] [\xd2] [\xaf] [ш] [і] [н] [ ] [\xd3] [\xa9] [з] [ с] [ал] [ма] [\xd2] [\x9b] [т] [ар] [ы] [н] [ т] [\xd2] [\xaf] [з] [ет] [у] [ а] [р] [\xd2] [\x9b] [ы] [л] [ы] [ о] [\xd2] [\x9b] [ид] [ы] [.]
- o200k_base (29): [Н] [ей] [рон] [дық] [ жел] [і] [ болж] [ам] [ мен] [ дұрыс] [ жауап] [ арас] [ындағы] [ қат] [ені] [ аз] [ай] [ту] [ үшін] [ өз] [ сал] [мақ] [тарын] [ түз] [ету] [ арқылы] [ оқ] [иды] [.]

**kk-lat** — `Neırondyq jeli boljam men durys jaýap arasyndaǵy qateni azaıtý úshin óz salmaqtaryn túzetý arqyly oqıdy.`

- r50k_base (58): [Ne] [ı] [r] [ond] [y] [q] [ j] [eli] [ bol] [jam] [ men] [ dur] [ys] [ ja] [\xc3] [\xbd] [ap] [ ar] [asy] [nda] [\xc7] [\xb5] [y] [ q] [aten] [i] [ a] [za] [ı] [t] [\xc3] [\xbd] [\x20\xc3] [\xba] [sh] [in] [\x20\xc3] [\xb3] [z] [ sal] [ma] [qt] [aryn] [ t] [ú] [z] [et] [\xc3] [\xbd] [ ar] [q] [y] [ly] [ o] [q] [ı] [dy] [.]
- cl100k_base (51): [Ne] [ır] [ond] [y] [q] [ j] [eli] [ bol] [jam] [ men] [ dur] [ys] [ ja] [ý] [ap] [ ar] [asy] [nda] [\xc7] [\xb5] [y] [ q] [aten] [i] [ a] [za] [ı] [t] [ý] [ ú] [sh] [in] [ ó] [z] [ sal] [ma] [qt] [ary] [n] [ tú] [zet] [ý] [ ar] [q] [y] [ly] [ o] [q] [ı] [dy] [.]
- o200k_base (42): [Ne] [ır] [ond] [y] [q] [ j] [eli] [ bol] [jam] [ men] [ dur] [ys] [ ja] [ý] [ap] [ arasynda] [\xc7] [\xb5] [y] [ qat] [eni] [ aza] [ıt] [ý] [ ú] [shin] [ ó] [z] [ sal] [ma] [qt] [aryn] [ tú] [zet] [ý] [ ar] [qy] [ly] [ oq] [ı] [dy] [.]

## Текст 5

**en** — `Spring came early that year, and the old garden behind the house slowly filled with the smell of apple blossoms.`

- r50k_base (23): [Spring] [ came] [ early] [ that] [ year] [,] [ and] [ the] [ old] [ garden] [ behind] [ the] [ house] [ slowly] [ filled] [ with] [ the] [ smell] [ of] [ apple] [ bloss] [oms] [.]
- cl100k_base (23): [Spring] [ came] [ early] [ that] [ year] [,] [ and] [ the] [ old] [ garden] [ behind] [ the] [ house] [ slowly] [ filled] [ with] [ the] [ smell] [ of] [ apple] [ bloss] [oms] [.]
- o200k_base (22): [Spring] [ came] [ early] [ that] [ year] [,] [ and] [ the] [ old] [ garden] [ behind] [ the] [ house] [ slowly] [ filled] [ with] [ the] [ smell] [ of] [ apple] [ blossoms] [.]

**ru** — `Весна в тот год пришла рано, и старый сад за домом медленно наполнился запахом яблоневого цвета.`

- r50k_base (104): [\xd0] [\x92] [е] [с] [н] [а] [\x20\xd0] [\xb2] [ ] [т] [о] [т] [\x20\xd0] [\xb3] [\xd0\xbe\xd0] [\xb4] [\x20\xd0] [\xbf] [р] [и] [\xd1] [\x88] [л] [а] [ ] [р] [а] [н] [о] [,] [\x20\xd0] [\xb8] [ ] [с] [т] [а] [р] [ы] [\xd0] [\xb9] [ ] [с] [а] [д] [\x20\xd0] [\xb7] [а] [\x20\xd0] [\xb4] [\xd0\xbe\xd0] [\xbc] [\xd0\xbe\xd0] [\xbc] [\x20\xd0] [\xbc] [е] [д] [л] [е] [н] [н] [о] [\x20\xd0] [\xbd] [а] [\xd0] [\xbf] [\xd0\xbe\xd0] [\xbb] [н] [и] [л] [с] [я] [\x20\xd0] [\xb7] [а] [\xd0] [\xbf] [а] [\xd1] [\x85] [\xd0\xbe\xd0] [\xbc] [ ] [я] [\xd0] [\xb1] [л] [о] [н] [е] [в] [\xd0\xbe\xd0] [\xb3] [о] [ ] [\xd1] [\x86] [в] [е] [т] [а] [.]
- cl100k_base (48): [В] [ес] [на] [ в] [ т] [от] [ г] [од] [ при] [ш] [ла] [ р] [ан] [о] [,] [ и] [ ст] [ар] [ый] [ с] [ад] [ за] [ д] [ом] [ом] [ м] [ед] [лен] [но] [ нап] [ол] [ни] [л] [ся] [ зап] [а] [х] [ом] [ я] [б] [л] [он] [ев] [ого] [ ц] [вет] [а] [.]
- o200k_base (30): [Вес] [на] [ в] [ тот] [ год] [ приш] [ла] [ ра] [но] [,] [ и] [ стар] [ый] [ сад] [ за] [ дом] [ом] [ мед] [ленно] [ нап] [ол] [ни] [лся] [ запах] [ом] [ яб] [лон] [евого] [ цвета] [.]

**ru-lat** — `Vesna v tot god prishla rano, i staryj sad za domom medlenno napolnilsya zapakhom yablonevogo tsveta.`

- r50k_base (43): [V] [es] [na] [ v] [ tot] [ god] [ pr] [ish] [la] [ ran] [o] [,] [ i] [ st] [ary] [j] [ sad] [ z] [a] [ dom] [om] [ med] [l] [enn] [o] [ nap] [oln] [il] [sy] [a] [ z] [ap] [akh] [om] [ y] [abl] [one] [v] [ogo] [ ts] [ve] [ta] [.]
- cl100k_base (40): [V] [es] [na] [ v] [ tot] [ god] [ pr] [ish] [la] [ r] [ano] [,] [ i] [ st] [ary] [j] [ sad] [ za] [ dom] [om] [ med] [len] [no] [ n] [apol] [nil] [s] [ya] [ zap] [akh] [om] [ y] [abl] [one] [v] [ogo] [ t] [sv] [eta] [.]
- o200k_base (39): [V] [es] [na] [ v] [ tot] [ god] [ pr] [ish] [la] [ rano] [,] [ i] [ st] [ary] [j] [ sad] [ za] [ dom] [om] [ med] [len] [no] [ nap] [ol] [n] [ils] [ya] [ zap] [akh] [om] [ y] [abl] [one] [v] [ogo] [ t] [sv] [eta] [.]

**kk** — `Бұл жылы көктем ерте келді, үйдің артындағы ескі бақ біртіндеп алма гүлінің иісіне толды.`

- r50k_base (109): [\xd0] [\x91] [\xd2] [\xb1] [л] [\x20\xd0] [\xb6] [ы] [л] [ы] [\x20\xd0] [\xba] [\xd3] [\xa9] [к] [т] [е] [м] [\x20\xd0] [\xb5] [р] [т] [е] [\x20\xd0] [\xba] [е] [л] [д] [\xd1] [\x96] [,] [ ] [\xd2] [\xaf] [\xd0] [\xb9] [д] [\xd1] [\x96] [\xd2] [\xa3] [\x20\xd0] [\xb0] [р] [т] [ы] [н] [д] [а] [\xd2] [\x93] [ы] [\x20\xd0] [\xb5] [с] [к] [\xd1] [\x96] [\x20\xd0] [\xb1] [а] [\xd2] [\x9b] [\x20\xd0] [\xb1] [\xd1] [\x96] [р] [т] [\xd1] [\x96] [н] [д] [е] [\xd0] [\xbf] [\x20\xd0] [\xb0] [л] [м] [а] [\x20\xd0] [\xb3] [\xd2] [\xaf] [л] [\xd1] [\x96] [н] [\xd1] [\x96] [\xd2] [\xa3] [\x20\xd0] [\xb8] [\xd1] [\x96] [с] [\xd1] [\x96] [н] [е] [ ] [т] [\xd0\xbe\xd0] [\xbb] [д] [ы] [.]
- cl100k_base (75): [Б] [\xd2] [\xb1] [л] [ ж] [ы] [л] [ы] [ к] [\xd3] [\xa9] [к] [т] [ем] [ е] [р] [те] [ к] [ел] [д] [і] [,] [ ] [\xd2] [\xaf] [й] [д] [і] [\xd2] [\xa3] [ а] [р] [ты] [н] [да] [\xd2] [\x93] [ы] [ е] [ск] [і] [ б] [а] [\xd2] [\x9b] [ б] [і] [р] [т] [і] [н] [д] [еп] [ а] [л] [ма] [ г] [\xd2] [\xaf] [л] [і] [н] [і] [\xd2] [\xa3] [ и] [і] [с] [і] [не] [ т] [ол] [д] [ы] [.]
- o200k_base (30): [Бұл] [ жылы] [ кө] [кт] [ем] [ ер] [те] [ кел] [ді] [,] [ үй] [дің] [ арт] [ындағы] [ е] [скі] [ бақ] [ бір] [т] [ін] [деп] [ алма] [ гүл] [інің] [ и] [іс] [іне] [ тол] [ды] [.]

**kk-lat** — `Bul jyly kóktem erte keldi, úıdiń artyndaǵy eski baq birtindep alma gúliniń ıisine toldy.`

- r50k_base (48): [Bul] [ j] [y] [ly] [ k] [ó] [k] [tem] [ er] [te] [ ke] [ld] [i] [,] [\x20\xc3] [\xba] [ı] [di] [\xc5] [\x84] [ ar] [ty] [nda] [\xc7] [\xb5] [y] [ es] [ki] [ ba] [q] [ b] [irt] [ind] [ep] [ al] [ma] [ g] [ú] [lin] [i] [\xc5] [\x84] [ ] [ı] [isine] [ told] [y] [.]
- cl100k_base (46): [B] [ul] [ j] [y] [ly] [ k] [ó] [k] [tem] [ ] [erte] [ k] [eld] [i] [,] [ ú] [ı] [di] [ń] [ ar] [ty] [nda] [\xc7] [\xb5] [y] [ es] [ki] [ ba] [q] [ b] [irt] [in] [dep] [ alma] [ g] [ú] [lin] [i] [ń] [ ] [ı] [is] [ine] [ told] [y] [.]
- o200k_base (37): [Bul] [ jy] [ly] [ k] [ók] [tem] [ er] [te] [ k] [eldi] [,] [ ú] [ı] [di] [ń] [ arty] [nda] [\xc7] [\xb5] [y] [ eski] [ ba] [q] [ birt] [ind] [ep] [ alma] [ g] [úl] [ini] [ń] [ ] [ı] [isine] [ told] [y] [.]

## Текст 6

**en** — `The meeting is on 15 March 2027 at 14:30, room 204; the price is 1,250 dollars.`

- r50k_base (24): [The] [ meeting] [ is] [ on] [ 15] [ March] [ 20] [27] [ at] [ 14] [:] [30] [,] [ room] [ 204] [;] [ the] [ price] [ is] [ 1] [,] [250] [ dollars] [.]
- cl100k_base (29): [The] [ meeting] [ is] [ on] [ ] [15] [ March] [ ] [202] [7] [ at] [ ] [14] [:] [30] [,] [ room] [ ] [204] [;] [ the] [ price] [ is] [ ] [1] [,] [250] [ dollars] [.]
- o200k_base (29): [The] [ meeting] [ is] [ on] [ ] [15] [ March] [ ] [202] [7] [ at] [ ] [14] [:] [30] [,] [ room] [ ] [204] [;] [ the] [ price] [ is] [ ] [1] [,] [250] [ dollars] [.]

**ru** — `Встреча состоится 15 марта 2027 года в 14:30 в аудитории 204; стоимость — 1250 долларов.`

- r50k_base (75): [\xd0] [\x92] [с] [т] [р] [е] [\xd1] [\x87] [а] [ ] [с] [о] [с] [т] [о] [и] [т] [с] [я] [ 15] [\x20\xd0] [\xbc] [а] [р] [т] [а] [ 20] [27] [\x20\xd0] [\xb3] [\xd0\xbe\xd0] [\xb4] [а] [\x20\xd0] [\xb2] [ 14] [:] [30] [\x20\xd0] [\xb2] [\x20\xd0] [\xb0] [у] [д] [и] [т] [о] [р] [и] [и] [ 204] [;] [ ] [с] [т] [о] [и] [м] [о] [с] [т] [ь] [ —] [ 12] [50] [\x20\xd0] [\xb4] [\xd0\xbe\xd0] [\xbb] [л] [а] [р] [\xd0\xbe\xd0] [\xb2] [.]
- cl100k_base (45): [В] [стр] [еч] [а] [ сост] [о] [ится] [ ] [15] [ м] [ар] [та] [ ] [202] [7] [ г] [ода] [ в] [ ] [14] [:] [30] [ в] [ а] [уд] [ит] [ор] [ии] [ ] [204] [;] [ ст] [о] [им] [ость] [ —] [ ] [125] [0] [ д] [ол] [л] [ар] [ов] [.]
- o200k_base (30): [В] [стреч] [а] [ состо] [ится] [ ] [15] [ марта] [ ] [202] [7] [ года] [ в] [ ] [14] [:] [30] [ в] [ аудит] [ории] [ ] [204] [;] [ стоимость] [ —] [ ] [125] [0] [ долларов] [.]

**ru-lat** — `Vstrecha sostoitsya 15 marta 2027 goda v 14:30 v auditorii 204; stoimost — 1250 dollarov.`

- r50k_base (33): [V] [stre] [cha] [ s] [ost] [o] [its] [ya] [ 15] [ mart] [a] [ 20] [27] [ god] [a] [ v] [ 14] [:] [30] [ v] [ auditor] [ii] [ 204] [;] [ sto] [im] [ost] [ —] [ 12] [50] [ dollar] [ov] [.]
- cl100k_base (37): [V] [stre] [cha] [ s] [osto] [its] [ya] [ ] [15] [ m] [arta] [ ] [202] [7] [ god] [a] [ v] [ ] [14] [:] [30] [ v] [ auditor] [ii] [ ] [204] [;] [ sto] [im] [ost] [ —] [ ] [125] [0] [ dollar] [ov] [.]
- o200k_base (37): [V] [stre] [cha] [ s] [osto] [its] [ya] [ ] [15] [ m] [arta] [ ] [202] [7] [ god] [a] [ v] [ ] [14] [:] [30] [ v] [ auditor] [ii] [ ] [204] [;] [ sto] [im] [ost] [ —] [ ] [125] [0] [ dollar] [ov] [.]

**kk** — `Кездесу 2027 жылғы 15 наурызда сағат 14:30-да 204-аудиторияда өтеді; бағасы — 1250 доллар.`

- r50k_base (83): [\xd0] [\x9a] [е] [\xd0] [\xb7] [д] [е] [с] [у] [ 20] [27] [\x20\xd0] [\xb6] [ы] [л] [\xd2] [\x93] [ы] [ 15] [\x20\xd0] [\xbd] [а] [у] [р] [ы] [\xd0] [\xb7] [д] [а] [ ] [с] [а] [\xd2] [\x93] [а] [т] [ 14] [:] [30] [-] [д] [а] [ 204] [-] [а] [у] [д] [и] [т] [о] [р] [и] [я] [д] [а] [ ] [\xd3] [\xa9] [т] [е] [д] [\xd1] [\x96] [;] [\x20\xd0] [\xb1] [а] [\xd2] [\x93] [а] [с] [ы] [ —] [ 12] [50] [\x20\xd0] [\xb4] [\xd0\xbe\xd0] [\xbb] [л] [а] [р] [.]
- cl100k_base (63): [К] [ез] [д] [ес] [у] [ ] [202] [7] [ ж] [ы] [л] [\xd2] [\x93] [ы] [ ] [15] [ на] [у] [ры] [з] [да] [ с] [а] [\xd2] [\x93] [ат] [ ] [14] [:] [30] [-] [да] [ ] [204] [-] [а] [уд] [ит] [ор] [ия] [да] [ ] [\xd3] [\xa9] [т] [ед] [і] [;] [ б] [а] [\xd2] [\x93] [ас] [ы] [ —] [ ] [125] [0] [ д] [ол] [л] [ар] [.]
- o200k_base (39): [К] [езд] [есу] [ ] [202] [7] [ жылғы] [ ] [15] [ на] [ур] [ыз] [да] [ са] [ғат] [ ] [14] [:] [30] [-] [да] [ ] [204] [-а] [уд] [ит] [ория] [да] [ өт] [еді] [;] [ бағ] [асы] [ —] [ ] [125] [0] [ доллар] [.]

**kk-lat** — `Kezdesý 2027 jylǵy 15 naýryzda saǵat 14:30-da 204-aýdıtorııada ótedi; baǵasy — 1250 dollar.`

- r50k_base (53): [K] [ez] [des] [\xc3] [\xbd] [ 20] [27] [ j] [yl] [\xc7] [\xb5] [y] [ 15] [ na] [\xc3] [\xbd] [ry] [z] [da] [ sa] [\xc7] [\xb5] [at] [ 14] [:] [30] [-] [da] [ 204] [-] [a] [\xc3] [\xbd] [d] [ı] [tor] [ı] [ı] [ada] [\x20\xc3] [\xb3] [ted] [i] [;] [ ba] [\xc7] [\xb5] [asy] [ —] [ 12] [50] [ dollar] [.]
- cl100k_base (52): [Ke] [z] [des] [ý] [ ] [202] [7] [ j] [yl] [\xc7] [\xb5] [y] [ ] [15] [ na] [ý] [ry] [z] [da] [ sa] [\xc7] [\xb5] [at] [ ] [14] [:] [30] [-da] [ ] [204] [-a] [ý] [d] [ı] [tor] [ı] [ı] [ada] [ ó] [ted] [i] [;] [ ba] [\xc7] [\xb5] [asy] [ —] [ ] [125] [0] [ dollar] [.]
- o200k_base (50): [K] [ez] [des] [ý] [ ] [202] [7] [ j] [yl] [\xc7] [\xb5] [y] [ ] [15] [ na] [ý] [ry] [z] [da] [ sa] [\xc7] [\xb5] [at] [ ] [14] [:] [30] [-da] [ ] [204] [-a] [ý] [dı] [tor] [ı] [ı] [ada] [ ót] [edi] [;] [ ba] [\xc7] [\xb5] [asy] [ —] [ ] [125] [0] [ dollar] [.]

## Текст 7

**en** — `Where is the nearest pharmacy? Go straight and turn left at the second traffic light.`

- r50k_base (17): [Where] [ is] [ the] [ nearest] [ pharmacy] [?] [ Go] [ straight] [ and] [ turn] [ left] [ at] [ the] [ second] [ traffic] [ light] [.]
- cl100k_base (17): [Where] [ is] [ the] [ nearest] [ pharmacy] [?] [ Go] [ straight] [ and] [ turn] [ left] [ at] [ the] [ second] [ traffic] [ light] [.]
- o200k_base (17): [Where] [ is] [ the] [ nearest] [ pharmacy] [?] [ Go] [ straight] [ and] [ turn] [ left] [ at] [ the] [ second] [ traffic] [ light] [.]

**ru** — `Где ближайшая аптека? Идите прямо и поверните налево на втором светофоре.`

- r50k_base (79): [\xd0] [\x93] [д] [е] [\x20\xd0] [\xb1] [л] [и] [\xd0] [\xb6] [а] [\xd0] [\xb9] [\xd1] [\x88] [а] [я] [\x20\xd0] [\xb0] [\xd0] [\xbf] [т] [е] [к] [а] [?] [\x20\xd0] [\x98] [д] [и] [т] [е] [\x20\xd0] [\xbf] [р] [я] [м] [о] [\x20\xd0] [\xb8] [\x20\xd0] [\xbf] [\xd0\xbe\xd0] [\xb2] [е] [р] [н] [и] [т] [е] [\x20\xd0] [\xbd] [а] [л] [е] [в] [о] [\x20\xd0] [\xbd] [а] [\x20\xd0] [\xb2] [т] [о] [р] [\xd0\xbe\xd0] [\xbc] [ ] [с] [в] [е] [т] [о] [\xd1] [\x84] [о] [р] [е] [.]
- cl100k_base (41): [Г] [де] [ б] [ли] [ж] [ай] [ш] [ая] [ а] [п] [т] [ек] [а] [?] [ И] [д] [ите] [ пр] [я] [м] [о] [ и] [ пов] [ер] [н] [ите] [ на] [л] [ев] [о] [ на] [ в] [тор] [ом] [ св] [ет] [о] [ф] [ор] [е] [.]
- o200k_base (23): [Г] [де] [ ближай] [шая] [ ап] [те] [ка] [?] [ И] [дите] [ прямо] [ и] [ повер] [ните] [ нал] [ево] [ на] [ втором] [ св] [ето] [ф] [оре] [.]

**ru-lat** — `Gde blizhajshaya apteka? Idite pryamo i povernite nalevo na vtorom svetofore.`

- r50k_base (32): [G] [de] [ bl] [iz] [h] [aj] [sh] [aya] [ apt] [eka] [?] [ Id] [ite] [ p] [ry] [amo] [ i] [ po] [vern] [ite] [ n] [ale] [vo] [ na] [ v] [tor] [om] [ s] [ve] [to] [fore] [.]
- cl100k_base (30): [G] [de] [ bl] [iz] [h] [aj] [sh] [aya] [ apt] [eka] [?] [ Id] [ite] [ pry] [amo] [ i] [ p] [overn] [ite] [ nale] [vo] [ na] [ v] [tor] [om] [ sv] [et] [of] [ore] [.]
- o200k_base (29): [G] [de] [ bl] [izh] [aj] [sh] [aya] [ ap] [te] [ka] [?] [ Id] [ite] [ pry] [amo] [ i] [ po] [vern] [ite] [ nale] [vo] [ na] [ v] [tor] [om] [ svet] [of] [ore] [.]

**kk** — `Ең жақын дәріхана қайда? Тіке жүріңіз де, екінші бағдаршамнан солға бұрылыңыз.`

- r50k_base (101): [\xd0] [\x95] [\xd2] [\xa3] [\x20\xd0] [\xb6] [а] [\xd2] [\x9b] [ы] [н] [\x20\xd0] [\xb4] [\xd3] [\x99] [р] [\xd1] [\x96] [\xd1] [\x85] [а] [н] [а] [ ] [\xd2] [\x9b] [а] [\xd0] [\xb9] [д] [а] [?] [\x20\xd0] [\xa2] [\xd1] [\x96] [к] [е] [\x20\xd0] [\xb6] [\xd2] [\xaf] [р] [\xd1] [\x96] [\xd2] [\xa3] [\xd1] [\x96] [\xd0] [\xb7] [\x20\xd0] [\xb4] [е] [,] [\x20\xd0] [\xb5] [к] [\xd1] [\x96] [н] [\xd1] [\x88] [\xd1] [\x96] [\x20\xd0] [\xb1] [а] [\xd2] [\x93] [д] [а] [р] [\xd1] [\x88] [а] [м] [н] [а] [н] [ ] [с] [\xd0\xbe\xd0] [\xbb] [\xd2] [\x93] [а] [\x20\xd0] [\xb1] [\xd2] [\xb1] [р] [ы] [л] [ы] [\xd2] [\xa3] [ы] [\xd0] [\xb7] [.]
- cl100k_base (70): [Е] [\xd2] [\xa3] [ ж] [а] [\xd2] [\x9b] [ы] [н] [ д] [\xd3] [\x99] [р] [і] [х] [ан] [а] [ ] [\xd2] [\x9b] [ай] [да] [?] [ Т] [і] [ке] [ ж] [\xd2] [\xaf] [р] [і] [\xd2] [\xa3] [і] [з] [ д] [е] [,] [ е] [к] [і] [н] [ш] [і] [ б] [а] [\xd2] [\x93] [д] [ар] [ш] [ам] [н] [ан] [ с] [ол] [\xd2] [\x93] [а] [ б] [\xd2] [\xb1] [ры] [л] [ы] [\xd2] [\xa3] [ы] [з] [.]
- o200k_base (30): [Е] [ң] [ жақ] [ын] [ дәр] [іх] [ана] [ қай] [да] [?] [ Т] [і] [ке] [ жүр] [іңіз] [ де] [,] [ е] [кінші] [ бағдар] [ш] [ам] [нан] [ сол] [ға] [ бұ] [р] [ылы] [ңыз] [.]

**kk-lat** — `Eń jaqyn dárihana qaıda? Tike júrińiz de, ekinshi baǵdarshamnan solǵa burylyńyz.`

- r50k_base (46): [E] [\xc5] [\x84] [ j] [aq] [yn] [ d] [á] [ri] [h] [ana] [ q] [a] [ı] [da] [?] [ T] [ike] [ j] [ú] [ri] [\xc5] [\x84] [iz] [ de] [,] [ e] [kins] [hi] [ ba] [\xc7] [\xb5] [d] [ars] [ham] [nan] [ sol] [\xc7] [\xb5] [a] [ bury] [ly] [\xc5] [\x84] [yz] [.]
- cl100k_base (41): [E] [ń] [ ja] [q] [yn] [ d] [á] [ri] [hana] [ qa] [ı] [da] [?] [ T] [ike] [ j] [ú] [ri] [ń] [iz] [ de] [,] [ e] [kin] [shi] [ ba] [\xc7] [\xb5] [dar] [sh] [am] [nan] [ sol] [\xc7] [\xb5] [a] [ bury] [ly] [ń] [yz] [.]
- o200k_base (37): [E] [ń] [ ja] [q] [yn] [ d] [ári] [hana] [ qa] [ıda] [?] [ T] [ike] [ jú] [ri] [ń] [iz] [ de] [,] [ ek] [inshi] [ ba] [\xc7] [\xb5] [dar] [sh] [am] [nan] [ sol] [\xc7] [\xb5] [a] [ bury] [ly] [ń] [yz] [.]
