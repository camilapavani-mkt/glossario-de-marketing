const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [,,html,out,n]=process.argv;fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+html);await p.evaluate(()=>document.fonts.ready);
await p.evaluate(()=>document.getAnimations().forEach(a=>a.pause()));
for(let i=0;i<+n;i++){await p.evaluate(t=>document.getAnimations().forEach(a=>a.currentTime=t),i*1000/30);
await p.screenshot({path:`${out}/f${String(i).padStart(4,'0')}.png`});}
await b.close();})();
