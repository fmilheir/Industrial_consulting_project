(function(){"use strict";var e={1720:function(e,t,n){var r=n(7764),o=n(4108);const i={id:"app"};function a(e,t,n,r,a,u){const c=(0,o.E1)("navbar"),l=(0,o.E1)("router-view");return(0,o.Wz)(),(0,o.An)("div",i,[e.$route.meta.hideMenu?(0,o.g1)("",!0):((0,o.Wz)(),(0,o.Az)(c,{key:0})),(0,o.K2)(l)])}var u=n(9096);const c={class:"top-0 left-0 right-0 shadow-md p-6 bg-gray-500 bg-opacity-100 rounded-b-lg"},l={class:"flex justify-center space-x-4"};function f(e,t,n,r,i,a){const f=(0,o.E1)("router-link");return(0,o.Wz)(),(0,o.An)("nav",c,[(0,o.QD)("ul",l,[(0,o.QD)("li",null,[(0,o.K2)(f,{to:"/dashboard"},{default:(0,o.Ql)((({isActive:e})=>[(0,o.QD)("a",{class:(0,u.WN)(["text-blue-300 hover:text-blue-500 font-semibold",e?"text-blue-700":""])},"Dashboard",2)])),_:1})]),(0,o.QD)("li",null,[(0,o.K2)(f,{to:"/about"},{default:(0,o.Ql)((({isActive:e})=>[(0,o.QD)("a",{class:(0,u.WN)(["text-blue-300 hover:text-blue-500 font-semibold",e?"text-blue-700":""])},"About",2)])),_:1})]),(0,o.QD)("li",null,[(0,o.K2)(f,{to:"/contact"},{default:(0,o.Ql)((({isActive:e})=>[(0,o.QD)("a",{class:(0,u.WN)(["text-blue-300 hover:text-blue-500 font-semibold",e?"text-blue-700":""])},"Contact",2)])),_:1})])])])}var s={name:"NavBar"},d=n(4100);const p=(0,d.c)(s,[["render",f],["__scopeId","data-v-2509eeba"]]);var h=p,v={name:"App",components:{navbar:h}};const b=(0,d.c)(v,[["render",a]]);var m=b,g=n(7464);const y=[{path:"/",name:"Main",component:()=>n.e(920).then(n.bind(n,7920)),meta:{hideMenu:!0}},{path:"/login",name:"Login",component:()=>n.e(684).then(n.bind(n,1684)),meta:{hideMenu:!0}},{path:"/signup",name:"SignUp",component:()=>n.e(544).then(n.bind(n,544)),meta:{hideMenu:!0}},{path:"/dashboard",name:"Dashboard",component:()=>n.e(108).then(n.bind(n,7108))},{path:"/about",name:"About",component:()=>n.e(224).then(n.bind(n,7224))},{path:"/contact",name:"Contact",component:()=>n.e(880).then(n.bind(n,6880))}],k=(0,g.gv)({history:(0,g.oz)("/"),routes:y});var x=k;(0,r.W0)(m).use(x).mount("#app")}},t={};function n(r){var o=t[r];if(void 0!==o)return o.exports;var i=t[r]={exports:{}};return e[r].call(i.exports,i,i.exports,n),i.exports}n.m=e,function(){var e=[];n.O=function(t,r,o,i){if(!r){var a=1/0;for(f=0;f<e.length;f++){r=e[f][0],o=e[f][1],i=e[f][2];for(var u=!0,c=0;c<r.length;c++)(!1&i||a>=i)&&Object.keys(n.O).every((function(e){return n.O[e](r[c])}))?r.splice(c--,1):(u=!1,i<a&&(a=i));if(u){e.splice(f--,1);var l=o();void 0!==l&&(t=l)}}return t}i=i||0;for(var f=e.length;f>0&&e[f-1][2]>i;f--)e[f]=e[f-1];e[f]=[r,o,i]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){n.f={},n.e=function(e){return Promise.all(Object.keys(n.f).reduce((function(t,r){return n.f[r](e,t),t}),[]))}}(),function(){n.u=function(e){return"js/"+e+"."+{108:"86d604de",224:"83a82214",544:"38cadeef",684:"5ac3523a",880:"7f4f8d1e",920:"4a880750"}[e]+".js"}}(),function(){n.miniCssF=function(e){return"css/"+e+".09f33192.css"}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={},t="industrial_consulting_project:";n.l=function(r,o,i,a){if(e[r])e[r].push(o);else{var u,c;if(void 0!==i)for(var l=document.getElementsByTagName("script"),f=0;f<l.length;f++){var s=l[f];if(s.getAttribute("src")==r||s.getAttribute("data-webpack")==t+i){u=s;break}}u||(c=!0,u=document.createElement("script"),u.charset="utf-8",u.timeout=120,n.nc&&u.setAttribute("nonce",n.nc),u.setAttribute("data-webpack",t+i),u.src=r),e[r]=[o];var d=function(t,n){u.onerror=u.onload=null,clearTimeout(p);var o=e[r];if(delete e[r],u.parentNode&&u.parentNode.removeChild(u),o&&o.forEach((function(e){return e(n)})),t)return t(n)},p=setTimeout(d.bind(null,void 0,{type:"timeout",target:u}),12e4);u.onerror=d.bind(null,u.onerror),u.onload=d.bind(null,u.onload),c&&document.head.appendChild(u)}}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.p="/"}(),function(){if("undefined"!==typeof document){var e=function(e,t,n,r,o){var i=document.createElement("link");i.rel="stylesheet",i.type="text/css";var a=function(n){if(i.onerror=i.onload=null,"load"===n.type)r();else{var a=n&&n.type,u=n&&n.target&&n.target.href||t,c=new Error("Loading CSS chunk "+e+" failed.\n("+a+": "+u+")");c.name="ChunkLoadError",c.code="CSS_CHUNK_LOAD_FAILED",c.type=a,c.request=u,i.parentNode&&i.parentNode.removeChild(i),o(c)}};return i.onerror=i.onload=a,i.href=t,n?n.parentNode.insertBefore(i,n.nextSibling):document.head.appendChild(i),i},t=function(e,t){for(var n=document.getElementsByTagName("link"),r=0;r<n.length;r++){var o=n[r],i=o.getAttribute("data-href")||o.getAttribute("href");if("stylesheet"===o.rel&&(i===e||i===t))return o}var a=document.getElementsByTagName("style");for(r=0;r<a.length;r++){o=a[r],i=o.getAttribute("data-href");if(i===e||i===t)return o}},r=function(r){return new Promise((function(o,i){var a=n.miniCssF(r),u=n.p+a;if(t(a,u))return o();e(r,u,null,o,i)}))},o={524:0};n.f.miniCss=function(e,t){var n={920:1};o[e]?t.push(o[e]):0!==o[e]&&n[e]&&t.push(o[e]=r(e).then((function(){o[e]=0}),(function(t){throw delete o[e],t})))}}}(),function(){var e={524:0};n.f.j=function(t,r){var o=n.o(e,t)?e[t]:void 0;if(0!==o)if(o)r.push(o[2]);else{var i=new Promise((function(n,r){o=e[t]=[n,r]}));r.push(o[2]=i);var a=n.p+n.u(t),u=new Error,c=function(r){if(n.o(e,t)&&(o=e[t],0!==o&&(e[t]=void 0),o)){var i=r&&("load"===r.type?"missing":r.type),a=r&&r.target&&r.target.src;u.message="Loading chunk "+t+" failed.\n("+i+": "+a+")",u.name="ChunkLoadError",u.type=i,u.request=a,o[1](u)}};n.l(a,c,"chunk-"+t,t)}},n.O.j=function(t){return 0===e[t]};var t=function(t,r){var o,i,a=r[0],u=r[1],c=r[2],l=0;if(a.some((function(t){return 0!==e[t]}))){for(o in u)n.o(u,o)&&(n.m[o]=u[o]);if(c)var f=c(n)}for(t&&t(r);l<a.length;l++)i=a[l],n.o(e,i)&&e[i]&&e[i][0](),e[i]=0;return n.O(f)},r=self["webpackChunkindustrial_consulting_project"]=self["webpackChunkindustrial_consulting_project"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=n.O(void 0,[999],(function(){return n(1720)}));r=n.O(r)})();
//# sourceMappingURL=app.6a515e9c.js.map