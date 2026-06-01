import json
leads = json.load(open("qualified_leads.json"))

T = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Route Exchange — Prime Pipeline</title>
<style>
:root{color-scheme:light;
  --bg:#eef1f7; --card:#ffffff; --ink:#0d1530; --ink2:#3a4561; --muted:#7b86a0; --line:#e6eaf2;
  --brand:#3552e6; --accent:#2f6bff; --win:#0f9d58; --warn:#f5a020; --hot:#ef4757; --violet:#7c5cff; --teal:#0fb5ba;
  --sh-sm:0 1px 2px rgba(13,21,48,.05); --sh:0 6px 22px rgba(13,21,48,.07); --sh-lg:0 14px 40px rgba(13,21,48,.12);
  --r:16px; --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;}
*{box-sizing:border-box;}
body{margin:0;background:radial-gradient(1200px 500px at 70% -120px,#dfe6fb 0%,var(--bg) 60%);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased;}
.wrap{max-width:1200px;margin:0 auto;padding:22px 22px 70px;}
a{color:var(--accent);text-decoration:none;}
.row{display:flex;align-items:center;gap:9px;}
.banner{display:none;background:#fdecec;border:1px solid #f5b5ad;color:#a3271a;padding:10px 13px;border-radius:12px;font-size:12.5px;margin:0 0 14px;}

/* HERO */
.hero{position:relative;overflow:hidden;border-radius:20px;padding:22px 24px;margin-bottom:18px;color:#eaf0ff;
  background:linear-gradient(135deg,#0a1230 0%,#16215a 48%,#23347e 100%);box-shadow:var(--sh-lg);}
.hero:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:26px 26px;mask:radial-gradient(420px 220px at 82% -40px,#000,transparent);}
.hero:after{content:"";position:absolute;right:-90px;top:-90px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(47,107,255,.55),transparent 65%);filter:blur(8px);}
.hero>*{position:relative;}
.eyebrow{display:flex;align-items:center;gap:9px;font-family:var(--mono);font-size:10.5px;letter-spacing:2px;text-transform:uppercase;color:#9fb0e6;}
.dot{width:8px;height:8px;border-radius:50%;background:#3ee08f;box-shadow:0 0 10px #3ee08f;animation:pulse 1.8s infinite;}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(62,224,143,.6);}70%{box-shadow:0 0 0 8px rgba(62,224,143,0);}100%{box-shadow:0 0 0 0 rgba(62,224,143,0);}}
.eyebrow .stamp{margin-left:auto;color:#cdd9ff;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:6px;padding:3px 9px;letter-spacing:.6px;text-transform:none;}
.mission{font-size:33px;line-height:1.06;font-weight:800;letter-spacing:-1px;margin:12px 0 4px;}
.mission .hl{background:linear-gradient(90deg,#7aa2ff,#3ee08f);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.missionsub{font-size:13px;color:#b9c5ec;max-width:760px;}
.missionsub b{color:#fff;}
.herostats{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:14px;margin-top:18px;}
@media(max-width:780px){.herostats{grid-template-columns:1fr 1fr;}}
.hs{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);border-radius:13px;padding:12px 14px;}
.hs .lab{font-size:10px;letter-spacing:.8px;text-transform:uppercase;color:#9fb0e6;}
.hs .val{font-family:var(--mono);font-size:23px;font-weight:700;margin-top:3px;}
.hs .val small{font-size:13px;color:#aebbe6;font-weight:500;}
.progress{height:10px;border-radius:6px;background:rgba(255,255,255,.16);overflow:hidden;position:relative;margin-top:9px;}
.progress i{display:block;height:100%;background:linear-gradient(90deg,#3ee08f,#7aa2ff);border-radius:6px;}
.progress .pace{position:absolute;top:-3px;bottom:-3px;width:2px;background:#ffd166;}
.hs .pacenote{font-size:10.5px;color:#aebbe6;margin-top:6px;}

/* SECTION HEADERS */
.sec{display:flex;align-items:center;gap:9px;margin:4px 2px 11px;}
.sec .ico{width:24px;height:24px;border-radius:7px;display:flex;align-items:center;justify-content:center;background:#e7ecfb;color:var(--brand);}
.sec h2{font-size:14px;font-weight:700;letter-spacing:-.2px;margin:0;color:var(--ink);}
.sec .hint{font-size:11.5px;color:var(--muted);font-weight:500;}
.sec .hint b{color:var(--ink2);}

/* DO NEXT */
.actions{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:20px;}
@media(max-width:880px){.actions{grid-template-columns:repeat(2,1fr);}}
@media(max-width:520px){.actions{grid-template-columns:1fr;}}
.act{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:15px 15px 13px;box-shadow:var(--sh-sm);cursor:pointer;transition:transform .12s,box-shadow .12s;position:relative;overflow:hidden;}
.act:hover{transform:translateY(-2px);box-shadow:var(--sh);}
.act .bar{position:absolute;left:0;top:0;bottom:0;width:4px;}
.act .top{display:flex;align-items:center;gap:10px;}
.act .badge{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex:none;}
.act .num{font-family:var(--mono);font-size:27px;font-weight:750;line-height:1;margin-left:auto;}
.act .ttl{font-size:13.5px;font-weight:700;margin-top:11px;}
.act .sub{font-size:11.5px;color:var(--muted);margin-top:1px;min-height:30px;}
.act .who{display:flex;flex-wrap:wrap;gap:4px;margin-top:9px;}
.act .who span{font-size:10.5px;background:#f1f4fb;border:1px solid var(--line);border-radius:6px;padding:2px 6px;color:var(--ink2);max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.act .go{font-size:11px;color:var(--accent);font-weight:600;margin-top:9px;display:inline-flex;gap:4px;align-items:center;}
.act.kick{grid-column:1/-1;background:linear-gradient(120deg,#101a3f,#22337a);color:#fff;border:none;}
.act.kick .ttl,.act.kick .num{color:#fff;} .act.kick .sub{color:#c4cef0;}

/* DAILY SCHEDULE */
.sched-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:18px;}
@media(max-width:880px){.sched-grid{grid-template-columns:repeat(3,1fr);}}
@media(max-width:520px){.sched-grid{grid-template-columns:1fr;}}
.sday{background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;box-shadow:var(--sh-sm);}
.sday.today-col{border:2px solid var(--brand);}
.sday-hd{padding:11px 13px;background:#f6f8fd;border-bottom:1px solid var(--line);}
.sday.today-col .sday-hd{background:linear-gradient(135deg,#0a1230 0%,#16215a 100%);border-bottom:none;}
.sday-hd-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:2px;}
.sday-name{font-size:10.5px;font-weight:600;color:var(--muted);}
.sday.today-col .sday-name{color:#9fb0e6;}
.sday-date{font-size:16px;font-weight:700;color:var(--ink);}
.sday.today-col .sday-date{color:#eaf0ff;}
.sday-tbadge{font-size:9px;font-weight:700;padding:2px 7px;border-radius:5px;background:rgba(255,255,255,.12);color:#c4d4ff;}
.spills{display:flex;gap:4px;flex-wrap:wrap;margin-top:7px;min-height:22px;}
.spill{font-size:9.5px;font-weight:700;padding:2px 7px;border-radius:10px;}
.spill.se{background:#e7ecfb;color:var(--brand);}
.spill.sl{background:#efe9ff;color:var(--violet);}
.spill.spost{background:#e3f6ec;color:var(--win);}
.sday.today-col .spill{background:rgba(255,255,255,.14);color:#c4d4ff;}
.sblock{padding:10px 13px;flex:1;}
.sblock:not(:last-child){border-bottom:1px solid var(--line);}
.stlbl{font-size:9.5px;font-weight:700;color:var(--muted);letter-spacing:.05em;text-transform:uppercase;margin-bottom:8px;}
.sact{display:flex;align-items:flex-start;gap:7px;font-size:12px;color:var(--ink2);margin-bottom:5px;line-height:1.4;}
.sact:last-child{margin-bottom:0;}
.sact.sm{color:var(--muted);}
.sact.sb{font-weight:700;color:var(--ink);}
.sdot{width:6px;height:6px;border-radius:1px;flex-shrink:0;margin-top:3px;}
.sd-blue{background:var(--accent);}
.sd-violet{background:var(--violet);}
.sd-amber{background:var(--warn);}
.sd-green{background:var(--win);}
/* today checklist */
.dchkcard{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:16px 18px;margin-bottom:18px;box-shadow:var(--sh-sm);}
.dchk-hd{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;}
.dchk-ttl{font-size:13.5px;font-weight:700;}
.dchk-prog{font-size:11.5px;color:var(--muted);}
.dchk-bar-bg{height:3px;background:#e6eaf2;border-radius:4px;margin-bottom:14px;}
.dchk-bar{height:3px;background:var(--brand);border-radius:4px;width:0%;transition:width .3s;}
.dchk-grid{display:grid;grid-template-columns:1fr 1fr;gap:2px 28px;}
@media(max-width:680px){.dchk-grid{grid-template-columns:1fr;}}
.dchk-sec{font-size:10px;font-weight:700;color:var(--muted);letter-spacing:.05em;text-transform:uppercase;margin-bottom:8px;}
.dchk-row{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--ink);padding:5px 0;cursor:pointer;}
.dchk-row input[type=checkbox]{accent-color:var(--brand);width:14px;height:14px;flex-shrink:0;cursor:pointer;}
.dchk-row.done{color:var(--muted);text-decoration:line-through;}
.dchk-acts{margin-top:12px;padding-top:11px;border-top:1px solid var(--line);display:flex;gap:7px;flex-wrap:wrap;}
.dchk-acts button.qa{font-size:11.5px;padding:6px 11px;border-radius:9px;border:1px solid var(--line);background:#fff;color:var(--ink2);cursor:pointer;font-weight:600;}
.dchk-acts button.qa:hover{background:#f5f7fc;}

/* CARDS / GRID */
.grid2{display:grid;grid-template-columns:1.25fr 1fr;gap:16px;margin-bottom:18px;}
@media(max-width:880px){.grid2{grid-template-columns:1fr;}}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:17px 19px;box-shadow:var(--sh-sm);margin-bottom:18px;}
.kpis{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-bottom:18px;}
@media(max-width:880px){.kpis{grid-template-columns:repeat(3,1fr);}}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:13px 14px;box-shadow:var(--sh-sm);}
.kpi .v{font-family:var(--mono);font-size:22px;font-weight:700;letter-spacing:-.5px;} .kpi .l{font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-top:3px;} .kpi .d{font-size:11px;color:var(--muted);margin-top:2px;}
/* funnel */
.fr{display:flex;align-items:center;gap:11px;margin-bottom:11px;}
.fr .name{width:96px;font-size:12.5px;color:var(--ink2);flex:none;font-weight:500;}
.fbar{flex:1;background:#eef1f8;border-radius:8px;height:26px;overflow:hidden;}
.ffill{height:100%;border-radius:8px;transition:width .6s cubic-bezier(.2,.8,.2,1);min-width:3px;}
.fr .cnt{width:118px;text-align:right;font-size:12.5px;flex:none;font-family:var(--mono);} .fr .cnt b{font-weight:700;} .fr .cnt .tg{color:var(--muted);}
.stagebars{display:flex;gap:10px;}
.stagebars .sb{flex:1;background:#f5f7fc;border:1px solid var(--line);border-radius:11px;padding:10px;text-align:center;}
.stagebars .sb .n{font-family:var(--mono);font-size:19px;font-weight:700;} .stagebars .sb .t{font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.4px;}
.chips{display:flex;flex-wrap:wrap;gap:8px;}
.chip{display:flex;align-items:center;gap:7px;background:#f5f7fc;border:1px solid var(--line);border-radius:9px;padding:7px 11px;font-size:12.5px;}
.chip .cd{width:9px;height:9px;border-radius:50%;}
/* cadence */
.flow{display:flex;gap:0;flex-wrap:wrap;}
.step{flex:1;min-width:120px;background:#f6f8fd;border:1px solid var(--line);border-radius:12px;padding:12px;position:relative;}
.step+.step{margin-left:26px;}
.step:not(:last-child):after{content:"";position:absolute;right:-19px;top:50%;width:12px;height:12px;transform:translateY(-50%) rotate(45deg);border-top:2px solid #cfd6e6;border-right:2px solid #cfd6e6;}
.step .day{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;}
.step .lbl{font-size:13px;font-weight:700;margin:3px 0 4px;display:flex;align-items:center;gap:6px;}
.tag{font-size:9.5px;padding:1px 6px;border-radius:5px;font-weight:700;text-transform:uppercase;letter-spacing:.3px;}
.tag.email{background:#e7ecfb;color:var(--brand);} .tag.li{background:#efe9ff;color:var(--violet);}
.step .pr{font-size:12px;color:var(--ink2);font-family:var(--mono);} .step .mini{height:5px;background:#e9edf6;border-radius:4px;margin-top:6px;overflow:hidden;} .step .mini i{display:block;height:100%;background:var(--brand);border-radius:4px;}
/* calendar */
.calwrap{display:grid;grid-template-columns:220px 1fr;gap:20px;}
@media(max-width:680px){.calwrap{grid-template-columns:1fr;}}
.calmonth{font-size:12.5px;font-weight:700;color:var(--ink2);margin-bottom:7px;text-align:center;}
.calgrid{width:100%;border-collapse:separate;border-spacing:3px;}
.calgrid th{font-size:9.5px;color:var(--muted);font-weight:600;text-align:center;}
.calgrid td{height:28px;text-align:center;font-size:11.5px;color:var(--ink2);border-radius:7px;background:#f5f7fc;position:relative;}
.calgrid td.muted{background:transparent;color:#cfd6e6;} .calgrid td.today{outline:2px solid var(--accent);color:var(--accent);font-weight:700;}
.calgrid td.has{background:#e3f6ec;color:var(--win);font-weight:700;}
.calgrid td.has:after{content:"";position:absolute;bottom:3px;left:50%;transform:translateX(-50%);width:5px;height:5px;border-radius:50%;background:var(--win);}
.agenda{list-style:none;margin:0;padding:0;}
.agenda li{display:flex;gap:11px;padding:9px 0;border-bottom:1px solid var(--line);font-size:12.8px;}
.agenda li:last-child{border-bottom:none;}
.agenda .ic{width:30px;height:30px;border-radius:9px;background:#e3f6ec;color:var(--win);display:flex;align-items:center;justify-content:center;flex:none;}
.empty{color:var(--muted);font-size:12.5px;padding:8px 0;}
/* legend */
details.legend{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--sh-sm);margin-bottom:18px;padding:0 18px;}
details.legend summary{cursor:pointer;list-style:none;padding:14px 0;font-size:13px;font-weight:700;display:flex;align-items:center;gap:9px;}
details.legend summary::-webkit-details-marker{display:none;}
.legrid{display:grid;grid-template-columns:1fr 1fr;gap:7px 22px;padding:0 0 16px;}
@media(max-width:680px){.legrid{grid-template-columns:1fr;}}
.legrid .li{display:flex;align-items:flex-start;gap:8px;font-size:12.3px;color:var(--ink2);}
.legrid .sw{width:11px;height:11px;border-radius:50%;flex:none;margin-top:3px;} .legrid .sq{width:11px;height:11px;border-radius:3px;flex:none;margin-top:3px;}
.legrid b{color:var(--ink);}
/* table */
.toolbar{display:flex;align-items:center;gap:8px;margin-bottom:12px;flex-wrap:wrap;}
.toolbar input{flex:1;min-width:170px;padding:9px 12px;border:1px solid var(--line);border-radius:10px;font-size:13px;background:#f8fafd;}
.toolbar select{padding:9px 11px;border:1px solid var(--line);border-radius:10px;font-size:13px;background:#fff;}
table.leads{width:100%;border-collapse:collapse;}
table.leads th,table.leads td{text-align:left;padding:9px 9px;font-size:12.5px;border-bottom:1px solid var(--line);vertical-align:top;}
table.leads th{color:var(--muted);font-weight:600;font-size:10.5px;text-transform:uppercase;letter-spacing:.4px;cursor:pointer;white-space:nowrap;}
table.leads tbody tr:hover{background:#f8fafd;}
td .co{font-weight:650;} td .em{color:var(--muted);font-size:11px;}
.pillb{display:inline-block;padding:3px 9px;border-radius:20px;font-size:11px;font-weight:600;white-space:nowrap;}
.tiergrow{background:#e7ecfb;color:var(--brand);} .tierhv{background:#e3f6ec;color:var(--win);} .tieratr{background:#fdecec;color:var(--hot);} .tierstd{background:#eef1f6;color:var(--muted);}
.seq{display:flex;gap:4px;}
.sp{font-size:9.5px;font-weight:800;width:23px;text-align:center;padding:3px 0;border-radius:6px;border:1px solid var(--line);color:#aeb6c8;background:#fff;}
.sp.done{color:#fff;border-color:transparent;} .sp.e.done{background:var(--brand);} .sp.l.done{background:var(--violet);}
.acts{display:flex;gap:4px;margin-top:6px;}
.acts button{font-size:10px;padding:3px 7px;border-radius:7px;border:1px solid var(--line);background:#fff;color:var(--ink2);cursor:pointer;font-weight:600;}
.acts button.on{color:#fff;border-color:transparent;} .acts button.li.on{background:var(--violet);} .acts button.opp.on{background:var(--warn);} .acts button.won.on{background:var(--win);} .acts button.no.on{background:var(--muted);}
.spin{display:inline-block;width:12px;height:12px;border:2px solid rgba(255,255,255,.4);border-top-color:#fff;border-radius:50%;animation:sp .8s linear infinite;vertical-align:-2px;}
@keyframes sp{to{transform:rotate(360deg);}}
details.editor{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--sh-sm);margin-bottom:18px;padding:0 18px;}
details.editor>summary{cursor:pointer;list-style:none;padding:15px 0;font-size:14px;font-weight:700;display:flex;align-items:center;gap:9px;}
details.editor>summary::-webkit-details-marker{display:none;}
.edhint{font-size:11.5px;color:var(--muted);margin-bottom:12px;}
.edhint code{background:#eef1f6;border-radius:4px;padding:1px 5px;font-size:11px;}
.edwrap{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:0 0 18px;}
@media(max-width:820px){.edwrap{grid-template-columns:1fr;}}
.edblock{margin-bottom:14px;}
.edblock .lab{font-size:11.5px;font-weight:700;color:var(--ink2);margin-bottom:5px;display:flex;align-items:center;gap:7px;}
.edblock .lab .pin{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.3px;background:#efe9ff;color:var(--violet);padding:1px 6px;border-radius:5px;}
.edblock input,.edblock textarea{width:100%;border:1px solid var(--line);border-radius:9px;padding:9px 11px;font-size:12.5px;font-family:inherit;background:#f8fafd;color:var(--ink);}
.edblock textarea{min-height:118px;resize:vertical;line-height:1.5;}
.edblock input{margin-bottom:6px;font-weight:600;}
.edside{align-self:start;position:sticky;top:8px;}
.edtools{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:10px;}
.edtools select{padding:8px 10px;border:1px solid var(--line);border-radius:9px;font-size:12.5px;background:#fff;flex:1;min-width:120px;}
.edtools button{padding:8px 12px;border:1px solid var(--line);border-radius:9px;font-size:12px;font-weight:600;background:#fff;color:var(--ink2);cursor:pointer;}
.edtools button.primary{background:var(--brand);color:#fff;border-color:transparent;}
.edprev{border:1px solid var(--line);border-radius:11px;background:#fbfcff;max-height:430px;overflow:auto;padding:4px 14px;}
.edprev .pe{padding:11px 0;border-bottom:1px solid var(--line);}
.edprev .pe:last-child{border-bottom:none;}
.edprev .pe .h{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.4px;color:var(--brand);}
.edprev .pe .s{font-size:12.5px;font-weight:700;margin:3px 0;}
.edprev .pe .b{font-size:12px;color:var(--ink2);white-space:pre-wrap;line-height:1.5;}
.genbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;background:#f1f5ff;border:1px solid #d9e2fb;border-radius:11px;padding:10px 13px;margin-bottom:12px;}
.genbar .gb-txt{font-size:12px;color:var(--ink2);}
.genbar .gb-txt b{color:var(--ink);}
.genbar button{padding:8px 13px;border-radius:9px;border:none;background:var(--brand);color:#fff;font-size:12px;font-weight:700;cursor:pointer;}
.genbar button:disabled{opacity:.5;cursor:default;}
.genbar .gstat{font-size:11.5px;color:var(--muted);}
.dchk{display:flex;align-items:center;gap:5px;font-size:10.5px;color:var(--muted);cursor:pointer;}
.dchk input{width:14px;height:14px;cursor:pointer;}
.draftedtag{display:inline-block;font-size:9.5px;font-weight:700;color:var(--win);background:#e3f6ec;border-radius:5px;padding:1px 6px;}
.edexport textarea{width:100%;min-height:84px;border:1px solid var(--line);border-radius:9px;padding:9px;font-size:11px;font-family:var(--mono);background:#f8fafd;margin-top:8px;color:var(--ink2);}
</style>
</head>
<body>
<div class="wrap">
  <div class="banner" id="banner"></div>

  <div class="hero">
    <div class="eyebrow"><span class="dot"></span> Route Exchange · Prime Contractor Acquisition <span class="stamp" id="updated">initializing <span class="spin"></span></span></div>
    <div class="mission">Sign <span class="hl">100 Prime Contractors</span></div>
    <div class="missionsub"><b>6%</b> blended close on <b>1,650</b> reached BSC operators · ICP: COO &amp; VP Ops, Enterprise 500+ / $20M+ · 8/day finishes ~Mar 2027, ~15/day closes inside 2026</div>
    <div class="herostats">
      <div class="hs"><div class="lab">Prospects reached</div><div class="val" id="hReached">0 <small>/ 1,650</small></div>
        <div class="progress"><i id="hFill" style="width:0%"></i><span class="pace" id="hPace"></span></div>
        <div class="pacenote" id="hPaceNote">staged &amp; ready</div></div>
      <div class="hs"><div class="lab">Closed</div><div class="val" id="hClosed">0 <small>/ 100</small></div></div>
      <div class="hs"><div class="lab">Proj. finish</div><div class="val" id="hProj" style="font-size:16px">—</div></div>
      <div class="hs"><div class="lab">Reached→closed</div><div class="val" id="hConv">—</div></div>
    </div>
  </div>

  <div class="sec"><span class="ico" id="icDo"></span><h2>Do Next</h2><span class="hint">your shortlist — tap a card to filter the leads below</span></div>
  <div class="actions" id="actions"></div>

  <!-- ── DAILY SCHEDULE ── -->
  <div class="sec"><span class="ico" id="icSched"></span><h2>This week's schedule</h2><span class="hint">11:00 am – 1:00 pm · <b id="schedToday">—</b></span></div>
  <div class="sched-grid" id="schedGrid"></div>
  <div class="dchkcard" id="todayChk">
    <div class="dchk-hd"><span class="dchk-ttl" id="dchkTitle">Today's checklist</span><span class="dchk-prog" id="dchkProg">0 of 5 done</span></div>
    <div class="dchk-bar-bg"><div class="dchk-bar" id="dchkBar"></div></div>
    <div class="dchk-grid" id="dchkGrid"></div>
    <div class="dchk-acts" id="dchkActs"></div>
  </div>
  <!-- ── END DAILY SCHEDULE ── -->

  <div class="kpis" id="kpis"></div>

  <div class="grid2">
    <div class="card"><div class="sec" style="margin-top:0"><span class="ico" id="icFun"></span><h2>Funnel to 100</h2><span class="hint">actual vs <b>6%</b> target</span></div><div id="funnel"></div></div>
    <div class="card"><div class="sec" style="margin-top:0"><span class="ico" id="icCh"></span><h2>Channels &amp; Replies</h2></div>
      <div class="stagebars" id="channels" style="margin-bottom:14px;"></div><div class="chips" id="replyChips"></div></div>
  </div>

  <div class="card"><div class="sec" style="margin-top:0"><span class="ico" id="icFlow"></span><h2>Outreach Cadence</h2><span class="hint">E1 + LinkedIn fire Day 0 (parallel) · bars show completion across loaded leads</span></div><div class="flow" id="flow"></div></div>

  <details class="editor" id="editorCard"><summary><span class="ico" id="icEdit" style="background:#efe9ff;color:var(--violet)"></span> Email Copy — edit &amp; preview <span style="font-weight:500;color:var(--muted);font-size:11.5px">· master template for all leads</span></summary>
    <div class="edhint">Tokens <code>{first_name}</code> and <code>{company}</code> fill per lead in the preview. Edits save automatically (this device). This is the <b>template</b> for every lead — for one-off per-lead changes use the markdown/CSV file. Hit <b>Copy edits</b> and paste back to me to push them into drafts.</div>
    <div class="edwrap">
      <div id="edFields"></div>
      <div class="edside">
        <div class="edtools"><span style="font-size:11.5px;color:var(--muted)">Preview as</span><select id="edLead"></select><button id="edReset">Reset</button><button class="primary" id="edCopy">Copy edits</button></div>
        <div class="edprev" id="edPrev"></div>
        <div class="edexport"><textarea id="edExport" readonly placeholder="Your edited copy as JSON — paste back to me to apply it."></textarea></div>
      </div>
    </div>
  </details>

  <div class="card"><div class="sec" style="margin-top:0"><span class="ico" id="icCal"></span><h2>Booked Demos</h2><span class="hint">live from your Calendar</span></div>
    <div class="calwrap"><div><div class="calmonth" id="calMonth"></div><div id="calGrid"></div></div>
      <div><ul class="agenda" id="agenda"><li class="empty">Loading&hellip;</li></ul></div></div></div>

  <details class="legend"><summary><span class="ico" id="icLeg" style="background:#eef1f6;color:var(--muted)"></span> Legend — how to read this</summary><div class="legrid" id="legend"></div></details>

  <div class="card" id="leadsCard"><div class="sec" style="margin-top:0"><span class="ico" id="icLead"></span><h2>Leads <span id="leadCount" style="color:var(--muted);font-weight:600"></span></h2><span class="hint">sequence pills = E1/LinkedIn/E2/E3 · buttons log LinkedIn / Opp / Won / Not-fit</span></div>
    <div class="genbar"><span class="gb-txt">Approve leads with the checkbox, then <b>generate E1 drafts</b> from the current editor copy (review in Gmail before sending).</span><button id="genDrafts">⚡ Generate E1 drafts</button><span class="gstat" id="genStat"></span></div>
    <div class="toolbar"><input id="search" placeholder="Search company, contact, city…">
      <select id="statusFilter"><option value="">All statuses</option><option value="closed">Closed (Prime)</option><option value="opp">Opportunity</option><option value="meeting">Meeting booked</option><option value="positive">Positive reply</option><option value="replied">Any reply</option><option value="linkedin">LinkedIn sent</option><option value="contacted">Emailed, awaiting</option><option value="new">Not contacted</option></select></div>
    <table class="leads"><thead><tr><th data-k="company">Company</th><th data-k="contact">Contact</th><th data-k="loc">Location</th><th data-k="icpTier">Tier</th><th>Sequence</th><th data-k="statusLabel">Status</th><th data-k="lastTs">Last</th><th>Draft?</th><th>Log</th></tr></thead><tbody id="rows"></tbody></table>
  </div>
</div>

<script>
const LEADS=__LEADS__;
const GMAIL_SEARCH="mcp__06051a5d-dff3-4536-9c02-b850bca9ace3__search_threads";
const CAL_EVENTS="mcp__b9e8ce76-5583-4e76-9686-4d5d7790991a__list_events";
const GMAIL_DRAFT="mcp__06051a5d-dff3-4536-9c02-b850bca9ace3__create_draft";
const CAL_IDS=["primary","getroute.com_8cpn29hr238lq73gi5611ssg6g@group.calendar.google.com"];
const DEMO_CAL="getroute.com_8cpn29hr238lq73gi5611ssg6g@group.calendar.google.com";
const US_DOMAINS=["getroute.com","rozaladocleaning.com","rozaladoservices.com","rozacontractors.com"];
const GOAL=1650, CLOSE_GOAL=100, DAILY=8, START=new Date("2026-06-01T00:00:00");
const REPLY_COLORS={positive:"var(--win)",negative:"var(--hot)",ooo:"var(--warn)",none:"#c2c7cd"};
const SL={closed:"Closed (Prime)",opp:"Opportunity",meeting:"Meeting booked",positive:"Positive reply",negative:"Declined",ooo:"Out of office",replied:"Replied",linkedin:"LinkedIn sent",contacted:"Awaiting reply",notfit:"Not a fit",new:"Not contacted"};
const SC={closed:"#0f9d58",opp:"#f5a020",meeting:"#0fb5ba",positive:"#2f6bff",negative:"#ef4757",ooo:"#c98a18",replied:"#5a6585",linkedin:"#7c5cff",contacted:"#7b86a0",notfit:"#9aa0a6",new:"#aeb6c8"};
const ICON={
 do:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 cal:'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
 mail:'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 link:'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>',
 target:'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg>',
 funnel:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 4h18l-7 8v7l-4 2v-9z"/></svg>',
 bolt:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10"/></svg>',
 flow:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h8a2 2 0 0 1 2 2v8"/></svg>',
 list:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>',
 info:'<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><line x1="12" y1="11" x2="12" y2="16"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
 sched:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="3" y1="10" x2="21" y2="10"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="7" y1="14" x2="7.01" y2="14" stroke-width="3"/><line x1="12" y1="14" x2="12.01" y2="14" stroke-width="3"/><line x1="7" y1="18" x2="7.01" y2="18" stroke-width="3"/><line x1="12" y1="18" x2="12.01" y2="18" stroke-width="3"/><line x1="17" y1="14" x2="17.01" y2="14" stroke-width="3"/></svg>'};

let STATE={}; try{STATE=JSON.parse(localStorage.getItem("rx_state")||"{}");}catch(e){STATE={};}
function st(id){return STATE[id]||(STATE[id]={});}
function toggle(id,k){const s=st(id);s[k]=!s[k];if(k==="closed"&&s[k])s.opp=true;localStorage.setItem("rx_state",JSON.stringify(STATE));compute();}
let APPTS=[], errs=[];
LEADS.forEach(l=>{l.domain=(l.email.split("@")[1]||"").toLowerCase();l.fn=((l.contact||"").replace(/\"/g,"").trim().split(/\s+/)[0])||"there";});
const byDomain={};LEADS.forEach(l=>{if(l.domain)byDomain[l.domain]=l;});

function unwrap(r){if(r==null)return{};if(typeof r==="string"){try{return JSON.parse(r);}catch(e){return{raw:r};}}
  if(r.content&&Array.isArray(r.content)){const t=r.content.map(c=>c&&c.text?c.text:"").join("");try{return JSON.parse(t);}catch(e){return{raw:t};}}
  if(r.result!==undefined)return unwrap(r.result);return r;}
async function callTool(n,a){try{const r=unwrap(await window.cowork.callMcpTool(n,a));if(r&&r.__error)errs.push(n.split("__")[2]||n);return r;}catch(e){errs.push((n.split("__")[2]||n));return{__error:String(e)};}}
function chunk(a,n){const o=[];for(let i=0;i<a.length;i+=n)o.push(a.slice(i,i+n));return o;}
function domainOf(x){if(!x)return"";const m=String(x).match(/[^@<\s]+@([^>\s]+)/);return m?m[1].toLowerCase():"";}
function isUs(x){return US_DOMAINS.includes(domainOf(x));}
function bizBetween(a,b){let d=new Date(a),n=0;while(d<b){if(d.getDay()%6!==0)n++;d=new Date(d.getTime()+864e5);}return n;}
function addBiz(a,n){let d=new Date(a),c=0;while(c<n){d=new Date(d.getTime()+864e5);if(d.getDay()%6!==0)c++;}return d;}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c]));}

async function loadGmail(){
  for(const g of chunk(LEADS.filter(l=>l.domain),8)){
    const q="newer_than:120d ("+g.map(l=>"from:"+l.domain+" OR to:"+l.domain).join(" OR ")+")";
    const res=await callTool(GMAIL_SEARCH,{query:q,pageSize:50});
    for(const th of ((res&&res.threads)||[])){
      const msgs=th.messages||[];let lead=null;
      for(const m of msgs){const d1=domainOf(m.sender);if(byDomain[d1]){lead=byDomain[d1];break;}
        for(const to of (m.toRecipients||[])){const d2=domainOf(to);if(byDomain[d2]){lead=byDomain[d2];break;}}if(lead)break;}
      if(!lead)continue;
      for(const m of msgs){const ts=Date.parse(m.date)||0;const fromUs=isUs(m.sender);const fromLead=domainOf(m.sender)===lead.domain;
        if(fromUs&&(m.toRecipients||[]).some(t=>domainOf(t)===lead.domain)){lead.contacted=true;lead.sentCount++;}
        if(fromLead){lead.replied=true;if(ts>lead.lastTs){lead.lastTs=ts;lead.lastSnippet=m.snippet||"";}}
        if(fromUs&&ts>lead.lastTs)lead.lastTs=ts;}
    }
  }
}
function heur(s){s=(s||"").toLowerCase();
  if(/out of office|ooo|on vacation|away from|parental leave|holiday|currently out/.test(s))return"ooo";
  if(/not interested|no thanks|unsubscribe|remove me|please stop|not a fit|do not contact|already have/.test(s))return"negative";
  if(/interested|sounds good|let'?s|happy to|schedule|book a|set up|calendar|works for me|tell me more|demo|available/.test(s))return"positive";
  return"neutral";}
async function classify(){
  const inb=LEADS.filter(l=>l.replied&&l.lastSnippet);if(!inb.length)return;
  try{if(window.cowork&&window.cowork.askClaude){
    const data=inb.map(l=>({company:l.company,reply:l.lastSnippet.slice(0,300)}));
    const out=await window.cowork.askClaude('Classify each reply sentiment as exactly one of: positive, negative, ooo, neutral. Return ONLY a JSON array of {"company","sentiment"} in order.',data);
    let p=typeof out==="string"?JSON.parse(out.replace(/```json|```/g,"").trim()):out;
    if(Array.isArray(p)){p.forEach((x,i)=>{if(inb[i])inb[i].sentiment=x.sentiment||"neutral";});return;}}
  }catch(e){}inb.forEach(l=>l.sentiment=heur(l.lastSnippet));}
async function loadCal(){
  const now=Date.now();const s=new Date(now-30*864e5).toISOString(),e=new Date(now+90*864e5).toISOString();const seen={};
  for(const cid of CAL_IDS){const res=await callTool(CAL_EVENTS,{calendarId:cid,startTime:s,endTime:e,pageSize:100,orderBy:"startTime"});
    for(const ev of ((res&&res.events)||[])){let m=null;
      for(const a of (ev.attendees||[])){const d=domainOf(a.email);if(byDomain[d]){m=byDomain[d];break;}}
      if(!m){const sum=(ev.summary||"").toLowerCase();for(const l of LEADS){const b=l.company.toLowerCase().split(/[ ,]/)[0];if(b.length>4&&sum.includes(b)){m=l;break;}}}
      const ts=Date.parse(ev.start&&(ev.start.dateTime||ev.start.date))||0;
      if(m){m.meeting=true;if(ts>m.lastTs)m.lastTs=ts;}
      if((m||cid===DEMO_CAL)&&ts){const key=ev.id||(ts+(ev.summary||""));if(!seen[key]){seen[key]=1;APPTS.push({start:ts,company:m?m.company:(ev.summary||"Demo"),url:ev.conferenceUrl||ev.htmlLink||""});}}
    }}
}
function statusOf(l){const s=st(l.id);
  if(s.closed)return"closed";if(s.opp)return"opp";if(l.meeting)return"meeting";
  if(l.replied&&l.sentiment==="positive")return"positive";if(l.replied&&l.sentiment==="negative")return"negative";
  if(l.replied&&l.sentiment==="ooo")return"ooo";if(l.replied)return"replied";
  if(s.notfit)return"notfit";if(s.linkedin)return"linkedin";if(l.contacted)return"contacted";return"new";}

function setIcons(){const m={icDo:ICON.do,icFun:ICON.funnel,icCh:ICON.bolt,icFlow:ICON.flow,icCal:ICON.cal,icLead:ICON.list,icLeg:ICON.info,icSched:ICON.sched};
  for(const k in m){const e=document.getElementById(k);if(e)e.innerHTML=m[k];}}

function focusLeads(f){const sel=document.getElementById("statusFilter");sel.value=f;renderTable();document.getElementById("leadsCard").scrollIntoView({behavior:"smooth",block:"start"});}

/* ── SCHEDULE ── */
const DAY_FULL=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
const SCHED_DEF=[
  {dow:1,name:"Monday",
   pills:[{t:"E1",c:"se"},{t:"LI msg",c:"sl"},{t:"LI post",c:"spost"}],
   b1:[{cls:"sb sd-amber",t:"Send E1 emails"},{cls:"sb sl sd-violet",t:"LinkedIn message"},{cls:"sm sd-green",t:"Actively engage"}],
   b2:[{cls:"sb sd-violet",t:"LinkedIn post"},{cls:"sm sd-green",t:"Reply to likes & comments"}],
   tasks11:["Send E1 emails to pipeline","LinkedIn messages — subcontracting outreach","Actively engage with connections"],
   tasks12:["Post LinkedIn content (subcontracting)","Engage with post likes & comments"]},
  {dow:2,name:"Tuesday",
   pills:[],
   b1:[{cls:"sd-amber",t:"Send follow-up emails"},{cls:"sm sd-green",t:"Actively engage"}],
   b2:[{cls:"sm sd-green",t:"Reply to likes & comments"}],
   tasks11:["Send follow-up emails","Actively engage with connections"],
   tasks12:["Reply to post likes & comments"]},
  {dow:3,name:"Wednesday",
   pills:[{t:"E3",c:"se"},{t:"LI msg",c:"sl"}],
   b1:[{cls:"sb sd-amber",t:"Send E3 emails"},{cls:"sb sd-violet",t:"LinkedIn message"},{cls:"sm sd-green",t:"Actively engage"}],
   b2:[{cls:"sm sd-green",t:"Reply to likes & comments"}],
   tasks11:["Send E3 emails to pipeline","LinkedIn messages — subcontracting outreach","Actively engage with connections"],
   tasks12:["Reply to post likes & comments"]},
  {dow:4,name:"Thursday",
   pills:[],
   b1:[{cls:"sd-amber",t:"Send follow-up emails"},{cls:"sm sd-green",t:"Actively engage"}],
   b2:[{cls:"sm sd-green",t:"Reply to likes & comments"}],
   tasks11:["Send follow-up emails","Actively engage with connections"],
   tasks12:["Reply to post likes & comments"]},
  {dow:5,name:"Friday",
   pills:[{t:"E5",c:"se"},{t:"LI msg",c:"sl"}],
   b1:[{cls:"sb sd-amber",t:"Send E5 emails"},{cls:"sb sd-violet",t:"LinkedIn message"},{cls:"sm sd-green",t:"Actively engage"}],
   b2:[{cls:"sm sd-green",t:"Reply to likes & comments"}],
   tasks11:["Send E5 emails to pipeline","LinkedIn messages — subcontracting outreach","Actively engage with connections"],
   tasks12:["Reply to post likes & comments"]}
];

function renderSchedule(){
  const now=new Date();
  const todayDow=now.getDay();
  // Find Monday of this week
  const mon=new Date(now);mon.setDate(now.getDate()-(todayDow===0?6:todayDow-1));
  const dayName=DAY_FULL[todayDow]||(todayDow===0||todayDow===6?"Weekend":"");
  const el=document.getElementById("schedToday");if(el)el.textContent=dayName||"Mon–Fri";
  let grid="";
  SCHED_DEF.forEach((day,i)=>{
    const date=new Date(mon);date.setDate(mon.getDate()+i);
    const isToday=date.toDateString()===now.toDateString();
    const dateStr=date.toLocaleDateString(undefined,{month:"short",day:"numeric"});
    grid+='<div class="sday'+(isToday?" today-col":"")+'"><div class="sday-hd"><div class="sday-hd-row"><span class="sday-name">'+day.name+'</span>'+(isToday?'<span class="sday-tbadge">Today</span>':'')+'</div><div class="sday-date">'+dateStr+'</div><div class="spills">'+day.pills.map(p=>'<span class="spill '+p.c+'">'+p.t+'</span>').join('')+'</div></div>';
    grid+='<div class="sblock"><div class="stlbl">11:00 – 12:00</div>'+day.b1.map(a=>'<div class="sact '+a.cls+'"><span class="sdot '+a.cls.split(" ")[1]+'"></span>'+esc(a.t)+'</div>').join('')+'</div>';
    grid+='<div class="sblock"><div class="stlbl">12:00 – 1:00</div>'+day.b2.map(a=>'<div class="sact '+a.cls+'"><span class="sdot '+a.cls.split(" ")[1]+'"></span>'+esc(a.t)+'</div>').join('')+'</div>';
    grid+='</div>';
  });
  const sg=document.getElementById("schedGrid");if(sg)sg.innerHTML=grid;
  // Build today checklist
  const todayDef=SCHED_DEF.find(d=>d.dow===todayDow);
  const chkCard=document.getElementById("todayChk");
  if(!todayDef){if(chkCard)chkCard.innerHTML='<div class="dchk-hd"><span class="dchk-ttl">No outreach today</span></div><p style="font-size:13px;color:var(--muted);margin:0">Outreach runs Monday – Friday, 11 am – 1 pm.</p>';return;}
  const seqTag=todayDef.pills.find(p=>p.t.startsWith("E"))||null;
  const ttlEl=document.getElementById("dchkTitle");if(ttlEl)ttlEl.textContent="Today's checklist — "+todayDef.name+(seqTag?" · "+seqTag.t:"");
  const KEY="rx_dchk_"+now.toLocaleDateString();
  let saved={};try{saved=JSON.parse(localStorage.getItem(KEY)||"{}");}catch(e){}
  const allTasks=[...todayDef.tasks11,...todayDef.tasks12];
  const TOTAL=allTasks.length;
  function countDone(){return allTasks.filter((_,i)=>saved["t"+i]).length;}
  function updBar(){const d=countDone();const bar=document.getElementById("dchkBar");const prog=document.getElementById("dchkProg");if(bar)bar.style.width=Math.round(d/TOTAL*100)+"%";if(prog)prog.textContent=d+" of "+TOTAL+" done";}
  function buildSec(tasks,label,offset){let h='<div class="dchk-sec">'+esc(label)+'</div>';tasks.forEach((t,i)=>{const ki="t"+(i+offset);h+='<label class="dchk-row'+(saved[ki]?" done":"")+'"><input type="checkbox"'+(saved[ki]?' checked="checked"':'')+' data-ki="'+ki+'"> '+esc(t)+'</label>';});return h;}
  const grid2=document.getElementById("dchkGrid");
  if(grid2)grid2.innerHTML='<div>'+buildSec(todayDef.tasks11,"11:00 – 12:00",0)+'</div><div>'+buildSec(todayDef.tasks12,"12:00 – 1:00",todayDef.tasks11.length)+'</div>';
  updBar();
  document.querySelectorAll("#dchkGrid .dchk-row input[type=checkbox]").forEach(cb=>{cb.addEventListener("change",()=>{saved[cb.dataset.ki]=cb.checked;cb.closest(".dchk-row").classList.toggle("done",cb.checked);localStorage.setItem(KEY,JSON.stringify(saved));updBar();});});
  const acts=document.getElementById("dchkActs");
  if(acts){acts.innerHTML='<button class="qa" onclick="focusLeads(\'new\')">View new leads →</button><button class="qa" onclick="focusLeads(\'positive\')">Book positive replies →</button><button class="qa" onclick="document.getElementById(\'editorCard\').open=true;document.getElementById(\'editorCard\').scrollIntoView({behavior:\'smooth\'})">Review email copy →</button>';}
}
/* ── END SCHEDULE ── */

function compute(){
  const reached=LEADS.filter(l=>{const s=st(l.id);return l.contacted||l.replied||l.meeting||s.linkedin||s.opp||s.closed;}).length;
  const d={reached,replies:LEADS.filter(l=>l.replied).length,meetings:LEADS.filter(l=>l.meeting).length,
    opps:LEADS.filter(l=>st(l.id).opp).length,closed:LEADS.filter(l=>st(l.id).closed).length,
    positive:LEADS.filter(l=>l.sentiment==="positive").length,emailed:LEADS.filter(l=>l.contacted).length,
    liSent:LEADS.filter(l=>st(l.id).linkedin).length,
    e1:LEADS.filter(l=>l.sentCount>=1).length,e2:LEADS.filter(l=>l.sentCount>=2).length,e3:LEADS.filter(l=>l.sentCount>=3).length};
  render(d);
}
let lastD={};
function render(d){lastD=d;
  const bn=document.getElementById("banner");
  if(errs.length){bn.style.display="";bn.innerHTML="⚠ Couldn't reach "+[...new Set(errs)].join(", ")+" — showing what loaded. Try Reload or re-check the connection.";}else bn.style.display="none";
  // hero
  const pct=Math.min(100,Math.round(d.reached/GOAL*100));
  document.getElementById("hReached").innerHTML=d.reached.toLocaleString()+' <small>/ 1,650</small>';
  document.getElementById("hFill").style.width=Math.max(pct,0.6)+"%";
  document.getElementById("hClosed").innerHTML=d.closed+' <small>/ 100</small>';
  document.getElementById("hConv").textContent=(d.reached?(d.closed/d.reached*100).toFixed(1):"0")+"%";
  const now=new Date();let expected=0,note="",proj="~Mar 2027";
  if(now<START){note="Kicks off Jun 1 — staged & ready";}
  else{const eb=bizBetween(START,now);expected=eb*DAILY;const rate=eb>0?d.reached/eb:0;
    if(rate>0)proj=addBiz(now,Math.ceil(Math.max(0,GOAL-d.reached)/rate)).toLocaleDateString(undefined,{month:"short",year:"2-digit"});
    const delta=d.reached-expected;note=(delta>=0?"On pace +":"Behind ")+Math.abs(delta)+" vs 8/day";}
  document.getElementById("hPaceNote").textContent=note;
  document.getElementById("hPace").style.left=Math.min(100,expected/GOAL*100)+"%";
  document.getElementById("hProj").textContent=proj;

  renderActions(d);
  renderSchedule();

  const replyRate=d.emailed?Math.round(d.replies/d.emailed*100):0;
  document.getElementById("kpis").innerHTML=[["Reached",d.reached,"of 1,650"],["Emailed",d.emailed,d.liSent+" on LinkedIn"],
    ["Replies",d.replies,replyRate+"% reply rate"],["Meetings",d.meetings,"demos"],["Opportunities",d.opps,"qualified"],
    ["Closed",d.closed,"of 100"]].map(k=>'<div class="kpi"><div class="v">'+k[1]+'</div><div class="l">'+k[0]+'</div><div class="d">'+k[2]+'</div></div>').join("");

  const fn=[["Reached",d.reached,GOAL,"#3552e6"],["Replied",d.replies,578,"#5b6ef0"],["Meetings",d.meetings,248,"#0fb5ba"],["Opps",d.opps,148,"#f5a020"],["Closed",d.closed,CLOSE_GOAL,"#0f9d58"]];
  document.getElementById("funnel").innerHTML=fn.map(s=>{const p=Math.min(100,Math.round(s[1]/s[2]*100));
    return '<div class="fr"><div class="name">'+s[0]+'</div><div class="fbar"><div class="ffill" style="width:'+Math.max(p,1.5)+'%;background:'+s[3]+'"></div></div><div class="cnt"><b>'+s[1]+'</b> <span class="tg">/ '+s[2]+'</span></div></div>';}).join("");

  document.getElementById("channels").innerHTML=[["Emails",d.emailed],["LinkedIn",d.liSent],["Reply %",replyRate+"%"]].map(c=>'<div class="sb"><div class="n">'+c[1]+'</div><div class="t">'+c[0]+'</div></div>').join("");
  const neg=LEADS.filter(l=>l.sentiment==="negative").length,ooo=LEADS.filter(l=>l.sentiment==="ooo").length,nore=Math.max(d.emailed-d.replies,0);
  document.getElementById("replyChips").innerHTML=[["Positive",d.positive,"positive"],["Negative",neg,"negative"],["OOO",ooo,"ooo"],["No response",nore,"none"]].map(r=>'<div class="chip"><span class="cd" style="background:'+REPLY_COLORS[r[2]]+'"></span>'+r[0]+' <b>'+r[1]+'</b></div>').join("");

  const flow=[{day:"Day 0",lbl:"Email 1",tag:"email",done:d.e1},{day:"Day 0",lbl:"LinkedIn DM",tag:"li",done:d.liSent},{day:"Day +3",lbl:"Email 2",tag:"email",done:d.e2},{day:"Day +7",lbl:"Email 3",tag:"email",done:d.e3}];
  document.getElementById("flow").innerHTML=flow.map(s=>'<div class="step"><div class="day">'+s.day+'</div><div class="lbl">'+s.lbl+' <span class="tag '+s.tag+'">'+(s.tag==="li"?"LinkedIn":"Email")+'</span></div><div class="pr">'+s.done+' / '+LEADS.length+'</div><div class="mini"><i style="width:'+Math.round(s.done/LEADS.length*100)+'%"></i></div></div>').join("");

  renderCalendar();renderLegend();renderTable();updateGenBar();
  document.getElementById("updated").innerHTML="updated "+new Date().toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"});
}
function renderActions(d){
  const P=l=>!st(l.id).notfit;
  const book=LEADS.filter(l=>l.sentiment==="positive"&&!l.meeting&&!st(l.id).closed);
  const fup=LEADS.filter(l=>l.contacted&&!l.replied&&!l.meeting&&P(l)&&l.sentCount<3);
  const li=LEADS.filter(l=>l.contacted&&!l.replied&&!st(l.id).linkedin&&P(l));
  const start=LEADS.filter(l=>!l.contacted&&!st(l.id).linkedin&&P(l));
  const C=document.getElementById("actions");
  const chips=arr=>arr.slice(0,4).map(l=>'<span>'+esc(l.company)+'</span>').join("")+(arr.length>4?'<span>+'+(arr.length-4)+' more</span>':"");
  const cards=[
    {n:book.length,t:"Book a demo",s:"Positive replies waiting on times",a:book,f:"positive",c:"var(--win)",bg:"#e3f6ec",ic:ICON.cal},
    {n:fup.length,t:"Send follow-up",s:"Emailed, no reply — next touch due",a:fup,f:"contacted",c:"var(--accent)",bg:"#e7ecfb",ic:ICON.mail},
    {n:li.length,t:"LinkedIn touch",s:"Send a 1:1 DM by hand",a:li,f:"contacted",c:"var(--violet)",bg:"#efe9ff",ic:ICON.link},
    {n:start.length,t:"Start outreach",s:"Fresh leads — aim 8/day",a:start,f:"new",c:"var(--warn)",bg:"#fdf0db",ic:ICON.target},
  ].filter(c=>c.n>0);
  if(!cards.length||(d.emailed===0&&d.liSent===0&&book.length===0&&fup.length===0&&li.length===0)){
    C.innerHTML='<div class="act kick"><div class="top"><div class="badge" style="background:rgba(255,255,255,.14);color:#fff">'+ICON.bolt+'</div><div class="num">10</div></div><div class="ttl">Kick off the campaign</div><div class="sub">Your 10 Email-1 drafts are in Gmail, ready to review &amp; send. Sending them starts the clock — replies, meetings and follow-ups light up here automatically.</div><div class="go">Open Gmail drafts →</div></div>'
    + (start.length?'<div class="act" data-f="new" style="margin-top:0"><span class="bar" style="background:var(--warn)"></span><div class="top"><div class="badge" style="background:#fdf0db;color:var(--warn)">'+ICON.target+'</div><div class="num">'+start.length+'</div></div><div class="ttl">Leads ready to email</div><div class="sub">Loaded &amp; qualified, not yet contacted.</div><div class="who">'+chips(start)+'</div><div class="go">View leads →</div></div>':"");
    C.querySelectorAll(".act[data-f]").forEach(el=>el.onclick=()=>focusLeads(el.dataset.f));
    return;
  }
  C.innerHTML=cards.map(c=>'<div class="act" data-f="'+c.f+'"><span class="bar" style="background:'+c.c+'"></span>'+
    '<div class="top"><div class="badge" style="background:'+c.bg+';color:'+c.c+'">'+c.ic+'</div><div class="num" style="color:'+c.c+'">'+c.n+'</div></div>'+
    '<div class="ttl">'+c.t+'</div><div class="sub">'+c.s+'</div><div class="who">'+chips(c.a)+'</div><div class="go">View →</div></div>').join("");
  C.querySelectorAll(".act[data-f]").forEach(el=>el.onclick=()=>focusLeads(el.dataset.f));
}
function renderCalendar(){
  const now=new Date();const fut=APPTS.filter(a=>a.start>=Date.now()-36e5).sort((x,y)=>x.start-y.start);
  const ag=document.getElementById("agenda");
  if(!fut.length)ag.innerHTML='<li class="empty">No demos booked yet. Positive replies → the daily task drafts a booking reply with 3 open slots; confirmed demos appear here.</li>';
  else ag.innerHTML=fut.slice(0,7).map(a=>{const d=new Date(a.start);return '<li><div class="ic">'+ICON.cal+'</div><div><b>'+d.toLocaleDateString(undefined,{weekday:"short",month:"short",day:"numeric"})+', '+d.toLocaleTimeString([],{hour:"numeric",minute:"2-digit"})+'</b><br>'+esc(a.company)+(a.url?' · <a href="'+esc(a.url)+'" target="_blank" rel="noopener">join</a>':'')+'</div></li>';}).join("");
  const y=now.getFullYear(),mo=now.getMonth();
  document.getElementById("calMonth").textContent=now.toLocaleDateString(undefined,{month:"long",year:"numeric"});
  const days={};APPTS.forEach(a=>{const d=new Date(a.start);if(d.getFullYear()===y&&d.getMonth()===mo)days[d.getDate()]=1;});
  const first=new Date(y,mo,1).getDay(),dim=new Date(y,mo+1,0).getDate(),td=now.getDate();
  let h='<table class="calgrid"><thead><tr><th>S</th><th>M</th><th>T</th><th>W</th><th>T</th><th>F</th><th>S</th></tr></thead><tbody><tr>';
  for(let i=0;i<first;i++)h+='<td class="muted"></td>';
  for(let dy=1;dy<=dim;dy++){const dow=(first+dy-1)%7;if(dy>1&&dow===0)h+='</tr><tr>';h+='<td class="'+(days[dy]?"has":(dy===td?"today":""))+'">'+dy+'</td>';}
  document.getElementById("calGrid").innerHTML=h+'</tr></tbody></table>';
}
function renderLegend(){
  const order=["closed","opp","meeting","positive","replied","linkedin","contacted","ooo","negative","notfit","new"];
  let h=order.map(s=>'<div class="li"><span class="sw" style="background:'+SC[s]+'"></span><span><b>'+SL[s]+'</b></span></div>').join("");
  h+='<div class="li"><span class="sq" style="background:#3552e6"></span><span><b>Sequence pills</b>: E1/E2/E3 = emails sent · Li = LinkedIn DM logged. Filled = done.</span></div>';
  h+='<div class="li"><span class="sq" style="background:#ffd166"></span><span><b>Yellow line</b> on the reached bar = where 8/day pace says you should be today.</span></div>';
  h+='<div class="li"><span class="sw" style="background:#0f9d58"></span><span><b>Reached</b> = any touch (email or LinkedIn) · <b>Closed</b> = signed Prime contractor.</span></div>';
  document.getElementById("legend").innerHTML=h;
}
let sortK="rank",sortDir=1;
const RANK={closed:0,opp:1,meeting:2,positive:3,replied:4,ooo:5,linkedin:6,contacted:7,negative:8,notfit:9,new:10};
function renderTable(){
  const q=(document.getElementById("search").value||"").toLowerCase(),sf=document.getElementById("statusFilter").value;
  let rows=LEADS.map(l=>{const s=statusOf(l);return{l,s,statusLabel:SL[s],rank:RANK[s],company:l.company,contact:l.contact,loc:(l.city?l.city+", ":"")+l.state,icpTier:l.icpTier,lastTs:l.lastTs||0,email:l.email};});
  if(q)rows=rows.filter(r=>(r.company+" "+r.contact+" "+r.loc+" "+r.email).toLowerCase().includes(q));
  if(sf)rows=rows.filter(r=>{const s=st(r.l.id);return sf==="closed"?s.closed:sf==="opp"?s.opp:sf==="meeting"?r.l.meeting:sf==="positive"?r.l.sentiment==="positive":sf==="replied"?r.l.replied:sf==="linkedin"?s.linkedin:sf==="contacted"?(r.l.contacted&&!r.l.replied):sf==="new"?!(r.l.contacted||s.linkedin):true;});
  rows.sort((a,b)=>{let x=a[sortK],y=b[sortK];if(typeof x==="string"){x=x.toLowerCase();y=(y||"").toLowerCase();}return(x>y?1:x<y?-1:0)*sortDir;});
  document.getElementById("leadCount").textContent="· "+rows.length+" shown / "+LEADS.length;
  const tc={Growth:"tiergrow","High Value":"tierhv","At-Risk":"tieratr",Standard:"tierstd"};
  document.getElementById("rows").innerHTML=rows.map(r=>{const col=SC[r.s],s=st(r.l.id),L=r.l;
    const pills='<div class="seq"><span class="sp e'+(L.sentCount>=1?" done":"")+'" title="Email 1">E1</span><span class="sp l'+(s.linkedin?" done":"")+'" title="LinkedIn">Li</span><span class="sp e'+(L.sentCount>=2?" done":"")+'" title="Email 2">E2</span><span class="sp e'+(L.sentCount>=3?" done":"")+'" title="Email 3">E3</span></div>';
    return '<tr><td><div class="co">'+esc(r.company)+'</div><div class="em">'+(L.website||"")+'</div></td><td>'+esc(r.contact)+'<div class="em">'+esc(r.email)+'</div></td><td>'+esc(r.loc)+'</td><td><span class="pillb '+(tc[r.icpTier]||"tierstd")+'">'+esc(r.icpTier||"—")+'</span></td><td>'+pills+'</td><td><span class="pillb" style="background:'+col+'1a;color:'+col+'">'+r.statusLabel+'</span></td><td style="font-family:var(--mono);color:var(--muted)">'+(r.lastTs?new Date(r.lastTs).toLocaleDateString(undefined,{month:"short",day:"numeric"}):"—")+'</td>'+'<td><label class="dchk"><input type="checkbox" class="appchk" data-id="'+L.id+'"'+(s.approved?" checked":"")+'>'+(s.drafted?'<span class="draftedtag">drafted</span>':'<span>draft?</span>')+'</label></td>'+'<td><div class="acts"><button class="li'+(s.linkedin?" on":"")+'" data-id="'+L.id+'" data-k="linkedin">Li</button><button class="opp'+(s.opp?" on":"")+'" data-id="'+L.id+'" data-k="opp">Opp</button><button class="won'+(s.closed?" on":"")+'" data-id="'+L.id+'" data-k="closed">Won</button><button class="no'+(s.notfit?" on":"")+'" data-id="'+L.id+'" data-k="notfit">No</button></div></td></tr>';}).join("")||'<tr><td colspan="9" class="empty">No leads match.</td></tr>';
  document.querySelectorAll(".acts button").forEach(b=>b.onclick=()=>toggle(+b.dataset.id,b.dataset.k));
  document.querySelectorAll(".appchk").forEach(c=>c.onchange=()=>{st(+c.dataset.id).approved=c.checked;localStorage.setItem("rx_state",JSON.stringify(STATE));renderActions(lastD||{});updateGenBar();});
}
document.querySelectorAll("th[data-k]").forEach(th=>th.onclick=()=>{const k=th.dataset.k==="statusLabel"?"rank":th.dataset.k;if(sortK===k)sortDir*=-1;else{sortK=k;sortDir=1;}renderTable();});
["search","statusFilter"].forEach(id=>{const el=document.getElementById(id);el.addEventListener("input",()=>{renderTable();try{localStorage.setItem("rxv_"+id,el.value);}catch(e){}});try{const v=localStorage.getItem("rxv_"+id);if(v!=null)el.value=v;}catch(e){}});

const SIG_T=`Stronger together,
Ricky

Ricky Regalado · Founder, Route (Exchange)
Owner, Rozalado Services (BSC) · ISSA board, BSC segment
getroute.com`;
const TOUCHES=[
 {k:"e1",lbl:"E1 — offer / request demo",pin:"Day 0",subj:true},
 {k:"li",lbl:"LinkedIn DM — parallel to E1",pin:"Day 0",subj:false},
 {k:"e2",lbl:"E2 — podcast / story invite",pin:"Day 3",subj:true},
 {k:"e3",lbl:"E3 — schedule demo",pin:"Day 7",subj:true},
 {k:"e5",lbl:"E5 — takeaway close",pin:"Day 13",subj:true}];
const DEFAULT_TPL={
 e1:{subj:"fellow BSC — talk shop?",body:`Hi {first_name},

I'm a fellow BSC owner (Rozalado Services) who has navigated the subcontracting model to scale from $1M to $35M across multiple markets — 20–30% YoY growth.

For over 10 years I've pressure-tested the subcontracting model and proven its worth to scale. Humbly, that success and tenure led me to a seat on the ISSA board, representing the BSC segment.

That role is grounded in giving the BSC community resources, guidance and tools — and it's exactly why I built Exchange: a tech-enabled growth platform for primes and subcontractors to win and grow together at ~20%.

I'd love to grab some time and walk you through the platform — and honestly, to get your perspective on subcontracting and talk shop.

If you're open, just reply and I'll send a couple of times that work.

${SIG_T}`},
 li:{subj:"",body:`Hi {first_name} — fellow BSC owner and ISSA board member here (I run Rozalado). Just sent you a quick note by email too. We're on a mission to improve the prime/sub model and debunk a few myths about it — built Exchange to do it. Would love to connect and talk shop. Stronger together — Ricky`},
 e2:{subj:"come share your story on Cleaning & Cocktails",body:`Hi {first_name},

Different note — no platform talk this time.

I host Cleaning & Cocktails, where operators trade the real stories of building a cleaning company — the wins, the scars, all of it. I'd love to have you on to share {company}'s story: how you've grown, what you've learned running the work, and your honest take on the prime/sub model.

No script, no pitch — just two BSC operators talking shop. Your story would mean a lot to the operators coming up behind you.

Grab a time that works and we'll record: [your podcast booking link]

${SIG_T}`},
 e3:{subj:"20 minutes on Exchange?",body:`Hi {first_name},

Following up — I'd still love to walk you through Exchange and get your read on it as a fellow prime.

Quick why-it's-worth-20-minutes: it's a tech-enabled growth platform that helps primes and subs win and grow together (~20% YoY), with vetting and compliance (COIs, W-9s, backgrounds) handled up front so the sub side stops being a liability.

Let's put 20 minutes on the calendar — grab whatever works: [your scheduling link]
Or reply with a day and I'll send a couple of times.

${SIG_T}`},
 e5:{subj:"should I close the loop?",body:`Hi {first_name},

I don't want to keep landing in your inbox, so I'll make this the last one.

If subcontracting-as-a-growth-engine isn't a priority right now, no worries at all — just say the word and I'll close the loop.

But if there's even a 15-minute version of this conversation worth having — your perspective for mine, peer to peer — I'll make the time this week. Just reply and it's yours.

Either way, I'm rooting for {company}. We're all stronger together.

${SIG_T}`}};
let TPL; try{TPL=JSON.parse(localStorage.getItem("rx_templates"));}catch(e){TPL=null;}
if(!TPL||!TPL.e1)TPL=JSON.parse(JSON.stringify(DEFAULT_TPL));
function saveTpl(){localStorage.setItem("rx_templates",JSON.stringify(TPL));document.getElementById("edExport").value=JSON.stringify(TPL,null,1);}
function tok(str,l){return (str||"").replace(/\{first_name\}/g,l?l.fn:"{first_name}").replace(/\{company\}/g,l?l.company:"{company}");}
function edPreview(){const id=+document.getElementById("edLead").value;const l=LEADS.find(x=>x.id===id)||LEADS[0];
  document.getElementById("edPrev").innerHTML=TOUCHES.map(t=>{const o=TPL[t.k]||{};
    return '<div class="pe"><div class="h">'+t.lbl+' · '+t.pin+'</div>'+(t.subj?'<div class="s">'+esc(tok(o.subj,l))+'</div>':'')+'<div class="b">'+esc(tok(o.body,l))+'</div></div>';}).join("");}
function buildEditor(){
  document.getElementById("icEdit").innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>';
  const F=document.getElementById("edFields");
  F.innerHTML=TOUCHES.map(t=>{const o=TPL[t.k]||{};
    return '<div class="edblock"><div class="lab">'+t.lbl+' <span class="pin">'+t.pin+'</span></div>'+
      (t.subj?'<input data-k="'+t.k+'" data-f="subj" value="'+esc(o.subj||"")+'" placeholder="Subject">':'')+
      '<textarea data-k="'+t.k+'" data-f="body" placeholder="Body">'+esc(o.body||"")+'</textarea></div>';}).join("");
  F.querySelectorAll("input,textarea").forEach(el=>el.addEventListener("input",()=>{const k=el.dataset.k,fld=el.dataset.f;if(!TPL[k])TPL[k]={};TPL[k][fld]=el.value;saveTpl();edPreview();}));
  const sel=document.getElementById("edLead");
  sel.innerHTML=LEADS.map(l=>'<option value="'+l.id+'">'+esc(l.company)+'</option>').join("");
  sel.addEventListener("change",edPreview);
  document.getElementById("edReset").onclick=()=>{if(confirm("Reset all email copy to the default template?")){TPL=JSON.parse(JSON.stringify(DEFAULT_TPL));saveTpl();buildEditor();edPreview();}};
  document.getElementById("edCopy").onclick=()=>{const t=document.getElementById("edExport");t.value=JSON.stringify(TPL,null,1);t.select();try{navigator.clipboard.writeText(t.value);}catch(e){}document.execCommand&&document.execCommand("copy");document.getElementById("edCopy").textContent="Copied ✓";setTimeout(()=>document.getElementById("edCopy").textContent="Copy edits",1600);};
  saveTpl();edPreview();
}


function updateGenBar(){const ap=LEADS.filter(l=>st(l.id).approved&&!st(l.id).drafted).length;const dn=LEADS.filter(l=>st(l.id).drafted).length;
  const b=document.getElementById("genDrafts");if(b){b.disabled=ap===0;b.textContent="⚡ Generate E1 drafts ("+ap+")";}
  const st2=document.getElementById("genStat");if(st2)st2.textContent=dn?dn+" drafted so far":"";}
async function generateDrafts(){
  const todo=LEADS.filter(l=>st(l.id).approved&&!st(l.id).drafted&&l.email);
  if(!todo.length){alert("Tick the Draft? box on the leads you want first.");return;}
  if(!confirm("Create Gmail drafts (Email 1) for "+todo.length+" approved lead(s)? They'll sit in your Gmail Drafts for review — nothing sends.")) return;
  const b=document.getElementById("genDrafts"),stat=document.getElementById("genStat");b.disabled=true;
  let ok=0;const li=[];
  for(let i=0;i<todo.length;i++){const l=todo[i];stat.textContent="creating "+(i+1)+"/"+todo.length+"…";
    const subj=tok((TPL.e1||{}).subj,l),body=tok((TPL.e1||{}).body,l);
    const r=await callTool(GMAIL_DRAFT,{to:[l.email],subject:subj,body:body});
    if(r&&(r.id||r.draftId||!r.__error)){st(l.id).drafted=true;ok++;li.push("• "+l.company+" ("+l.fn+"): "+tok((TPL.li||{}).body,l));}
  }
  localStorage.setItem("rx_state",JSON.stringify(STATE));
  const ex=document.getElementById("edExport");if(ex&&li.length){ex.value="LinkedIn DMs to send by hand (parallel to E1):\n\n"+li.join("\n\n");}
  stat.textContent=ok+" draft(s) created ✓ — check Gmail. LinkedIn DMs are in the editor's copy box.";
  compute();
}

function reset(){errs=[];APPTS=[];LEADS.forEach(l=>{l.contacted=false;l.sentCount=0;l.replied=false;l.sentiment="none";l.meeting=false;l.lastTs=0;l.lastSnippet="";});}
async function loadAll(){reset();try{await loadGmail();}catch(e){errs.push("Gmail");}try{await classify();}catch(e){}try{await loadCal();}catch(e){errs.push("Calendar");}compute();}
setIcons();buildEditor();document.getElementById("genDrafts").onclick=generateDrafts;reset();compute();loadAll();
setInterval(loadAll,90000);
</script>
</body></html>
"""
html=T.replace("__LEADS__",json.dumps(leads))
open("route_pipeline_dashboard.html","w").write(html)
print("bytes:",len(html))
