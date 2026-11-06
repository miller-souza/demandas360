const cols=["Em andamento","Aguardando priorização","Concluído"];
const board=document.querySelector("#board"), metrics=document.querySelector("#metrics");
const search=document.querySelector("#search"), area=document.querySelector("#area");
async function load(){
 const params=new URLSearchParams(); if(search.value)params.set("q",search.value);if(area.value)params.set("area",area.value);
 const [items,resumo]=await Promise.all([fetch("/api/demandas?"+params).then(r=>r.json()),fetch("/api/resumo").then(r=>r.json())]);
 metrics.innerHTML=[["Demandas",resumo.total],...cols.map(s=>[s,resumo.por_status[s]])].map(([k,v])=>`<article class="metric"><small>${k}</small><strong>${v}</strong></article>`).join("");
 board.innerHTML=cols.map(s=>`<section class="column"><h2>${s}<span class="count">${items.filter(x=>x.status===s).length}</span></h2>${items.filter(x=>x.status===s).map(x=>`<article class="ticket"><small>${x.id}</small><h3>${x.titulo}</h3><p>${x.descricao}</p><span class="tag">${x.area}</span></article>`).join("")||'<p class="count">Nenhuma demanda encontrada.</p>'}</section>`).join("");
}
fetch("/api/areas").then(r=>r.json()).then(xs=>xs.forEach(x=>area.add(new Option(x,x))));
search.addEventListener("input",load);area.addEventListener("change",load);document.querySelector("#reset").onclick=()=>{search.value="";area.value="";load()};load();
