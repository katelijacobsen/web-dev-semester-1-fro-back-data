/*
MIT License

Copyright (c) 2024 Santiago Donoso (mixhtml.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

// Create CSS
const css = `
#mix-cover{    
    position: fixed; top:0rem; left:0;
    width: 100vw;
    height: 0.3rem;
    background-color: rgb(6, 182, 212);
    z-index: 20;
}
.mix-hidden{
    display: none !important;
}
.mix-in{
    display: none;
    opacity: 0;
} 
.mix-error{
    background-color: rgba(230,130,130, 0.5);
}
.mix-fade-in-1000{ animation: mix-fade-in 1000ms forwards; }
.mix-fade-in-2000{ animation: mix-fade-in 2000ms forwards; }
.mix-fade-in-3000{ animation: mix-fade-in 3000ms forwards; }
.mix-fade-in-4000{ animation: mix-fade-in 4000ms forwards; }
.mix-fade-in-5000{ animation: mix-fade-in 5000ms forwards; }

.mix-fade-out-1000{ animation: mix-fade-out 1000ms forwards; }
.mix-fade-out-2000{ animation: mix-fade-out 2000ms forwards; }
.mix-fade-out-3000{ animation: mix-fade-out 3000ms forwards; }
.mix-fade-out-4000{ animation: mix-fade-out 4000ms forwards; }
.mix-fade-out-5000{ animation: mix-fade-out 5000ms forwards; }

@keyframes mix-fade-out {
    0% {
        opacity: 1;
    }
    100% {
        opacity: 0;
    }
}
@keyframes mix-fade-in { 0% { opacity: 0;}
    100% {
        opacity: 1;
    }
}
`
const style = document.createElement('style')
style.innerHTML = css
document.head.appendChild(style)

const intervals = []
const fades = [1000, 2000, 3000, 4000, 5000]
const DISPLAY_ERRORS = true
try{
    let mix_replace_url = document.querySelector("[mix-url]")
    if(mix_replace_url){
        mix_replace_url = mix_replace_url.getAttribute("mix-url")
        console.log(mix_replace_url)
        history.replaceState({"mix_page":mix_replace_url}, "title", mix_replace_url)
    }
    else{
        if(DISPLAY_ERRORS){ console.log("Single Page App not possible") }
    }
}catch(error){
    if(DISPLAY_ERRORS){ 
        console.log(error) 
        console.log(`Warning: Single Page App not possible, since mix_replace_url not set`)
    }
}
// ##############################
window.onpopstate = function(event){
    mix_switch_page(event.state.mix_page, false)
}
// ##############################
history.scrollRestoration = "manual"
let ignoreScroll = false
window.addEventListener("popstate", () => {
    ignoreScroll = true
    setTimeout(() => {
        ignoreScroll = false
    }, 100)
})
window.addEventListener("scroll", () => {
    try{
        if (ignoreScroll) return    
        document.querySelector("[mix-on='yes']").setAttribute("mix-y", window.scrollY) 
    }catch(error){
        if(DISPLAY_ERRORS){ console.log(error) }
    }
})
// ##############################
setInterval(async function(){
    try{
        document.querySelectorAll("[mix-ex]").forEach(el=>{
            if(el.getAttribute("mix-ttl")=="0"){
                return
            }
            if( el.getAttribute("mix-on") == "yes" ){
                el.setAttribute("mix-ex", el.getAttribute("mix-ttl"))
                return
            }
            let ex_time = el.getAttribute("mix-ex") - 1000
            if(ex_time <= 0){
                if(el.hasAttribute("mix-url")){
                    el.remove()                    
                }else{
                    el.remove()  
                }
                return
            }
            el.setAttribute("mix-ex", ex_time)
        })
    }catch(error){ 
        if(DISPLAY_ERRORS){ 
            console.error("setInterval for clearing pages", error) 
        }
    }
}, 1000)
// ##############################
function hide_elements(selectors){
    try{
        selectors = selectors.split(',')
        selectors.forEach(selector => {
            document.querySelectorAll(selector).forEach(i=>{                 
                i.classList.add("mix-hidden")
            })
        })
    }catch(error){
        if(DISPLAY_ERRORS){ console.log(error) }
    }
}

// ##############################
function show_elements(selectors){
    try{
        selectors = selectors.split(',')
        selectors.forEach(selector => {
            document.querySelectorAll(selector).forEach(i=>{                 
                i.classList.remove("mix-hidden")
            })
        })
    }catch(error){
        if(DISPLAY_ERRORS){ console.log(error) }
    }
}

// ##############################
function mix_switch_page(mix_page, push_to_history = true){
    try{
        el = document.querySelector(`[mix-url="${mix_page}"]`)
        if( ! el ){
            let el_cover = false
            const el = document.querySelector(`[href='${mix_page}']`)
            if( el.hasAttribute("mix-cover")){ 
                el_cover = document.querySelector(el.getAttribute("mix-cover"))
                el_cover.classList.remove("mix-hidden")
            }            
            mix_page += mix_page.includes("?") ? "&mix-page=yes" : "?mix-page=yes"
            mix_fetch(mix_page, "GET", null, false, el_cover, false)
            return
        }
        document.title = el.getAttribute("mix-title")
        if( ! el.getAttribute("mix-y") ){ el.setAttribute("mix-y", "0") }
        
        hide_elements(el.getAttribute("mix-hide"))
        show_elements(el.getAttribute("mix-show"))
        
        if(el.hasAttribute("mix-script")){
            const data = el.getAttribute("mix-script").trim()
            eval(data)
        }  
        document.querySelectorAll("[mix-on]").forEach(i=>{ i.setAttribute("mix-on", "no") })
        el.setAttribute("mix-on", "yes")  
        window.scrollTo(0, el.getAttribute("mix-y"))                
        if( push_to_history ){
            history.pushState({"mix_page":el.getAttribute("mix-url")}, "title", el.getAttribute("mix-url"))
        }
    }catch(error){ 
        if(DISPLAY_ERRORS){ 
            console.error("mix_switch_page()", error) 
        }
    }
}
// ##############################
let timeout = null
function mixhtml(){
    try{
        const el = event.target
        if( el.hasAttribute("mix-page") ){
            const href = el.getAttribute("href")
            const loaded_page = document.querySelector(`[mix-url="${href}"]`)
            if(loaded_page){ 
                if( loaded_page.getAttribute("mix-on") == "yes" ){
                    return
                }             
                mix_switch_page(loaded_page.getAttribute("mix-url"), true)
                return
             }
        }      
        let url = ""
        let method = "GET"
        let form = false
        let el_cover = false
        if( el.hasAttribute("mix-get") ){ url = el.getAttribute("mix-get"); method = "GET" }
        if( el.hasAttribute("mix-post") ){ url = el.getAttribute("mix-post"); method = "POST" }
        if( el.hasAttribute("mix-patch") ){ url = el.getAttribute("mix-patch"); method = "PATCH" }
        if( el.hasAttribute("mix-put") ){ url = el.getAttribute("mix-put"); method = "PUT" }
        if( el.hasAttribute("mix-delete") ){ url = el.getAttribute("mix-delete"); method = "DELETE" }
        if( el.hasAttribute("mix-cover")){ 
            el_cover = document.querySelector(el.getAttribute("mix-cover"))
            el_cover.classList.remove("mix-hidden")
        }
        if( el.hasAttribute("href") && url == "" ){ url = el.getAttribute("href") }
        if(el.tagName === "FORM"){
            if( el.hasAttribute("action") ){ 
                if( url == ""){ url = el.getAttribute("action") }                
            }
            if(["POST", "PUT", "PATCH"].includes(method)){
                let errors = false
                el.querySelectorAll("[mix-validate]").forEach(el=>{
                    el.classList.remove("mix-error")
                    const regex = el.getAttribute("mix-validate")                  
                    const re = new RegExp(regex)
                    if( ! re.test(el.value) ){
                        el.classList.add("mix-error") 
                        errors = true
                    }
                })                  
                if(errors) return
            } 
            form = el
        }
        if( (el.hasAttribute("mix-post") || el.hasAttribute("mix-put") || 
            el.hasAttribute("mix-patch") || el.hasAttribute("mix-delete")) && el.tagName !== "FORM" ){
            if(el.hasAttribute("mix-validate")){
                el.classList.remove("mix-error") 
                const regex = el.getAttribute("mix-validate")
                const re = new RegExp(regex)
                if( ! re.test(el.value) ){
                    el.classList.add("mix-error")
                    clearTimeout(timeout)
                    return
                }                
            }
            const newElement = el.cloneNode(true)
            let frm = document.createElement("form")
            frm.appendChild(newElement)         
            form = frm         
        }
        if( url == "" ){ console.error("mixhtml() - url missing"); return }
        if( el.hasAttribute("mix-page") ){ url += url.includes("?") ? "&mix-page=yes" : "?mix-page=yes" }

        if(el.hasAttribute("disabled")){
            el.preventDefault()
        }
        if(el.hasAttribute("mix-await")){
            el.innerHTML = el.getAttribute("mix-await")
            el.setAttribute("disabled", true)
        }

        if(form){
            if( el_await = form.querySelector("[mix-await]") ){
                el_await.innerHTML = el_await.getAttribute("mix-await")
                el_await.setAttribute("disabled", true)
            }
        }

        if( el.hasAttribute("mix-delay") ){
            clearTimeout(timeout)
            timeout = setTimeout(function(){
                console.log("x")
                mix_fetch(url, method, form, true, el_cover, el)
            }, el.getAttribute("mix-delay"))
        }else{
            mix_fetch(url, method, form, true, el_cover, el)
        }
    }catch(error){ 
        if(DISPLAY_ERRORS){ console.log(error) }
    }
}

// ##############################
async function mix_fetch(url, method, form, push_to_history=true, el_cover=false, el=false){
    try{
        let conn = null
        if( method == "GET" || method == "DELETE" ){
            conn = await fetch(url, {method:method})
        }
        if( method == "POST" || method == "PATCH" || method == "PUT" ){
            if( form ){
                conn = await fetch(url, {method:method, body: new FormData(form) })
            }else{
                conn = await fetch(url, {method:method})
            }              
        }
        if(el){
            if( el.hasAttribute("mix-await") ){
                el.innerHTML = el.getAttribute("mix-done")
                el.removeAttribute("disabled")
            }            
        }
        if(form){
            if( el_await = form.querySelector("[mix-await]") ){
                el_await.innerHTML = el_await.getAttribute("mix-done")
                el_await.removeAttribute("disabled")
            }
        }
        if(el_cover){
            el_cover.classList.add("mix-hidden")
        }
        const template = document.createElement("template")
        template.innerHTML = await conn.text()
        const t = template.content
        t.querySelectorAll("*").forEach(tag=>{
            if( tag.hasAttribute("mix-url") ){            
                document.title = tag.getAttribute("mix-title")
                if(push_to_history){
                    history.pushState({"mix_page":tag.getAttribute("mix-url")}, "title", tag.getAttribute("mix-url"))
                }

                hide_elements(tag.getAttribute("mix-hide"))
                show_elements(tag.getAttribute("mix-show"))

                document.querySelectorAll("[mix-on]").forEach(i=>{                 
                    i.setAttribute("mix-on", "no")
                })    
                window.scrollTo(0,0)                                            
            } 
            if( tag.hasAttribute("mix-before-begin") ){           
                document.querySelectorAll(tag.getAttribute("mix-before-begin")).forEach(el=>{                  
                    if( tag.hasAttribute("mix-url") ){
                        el.insertAdjacentHTML("beforebegin", tag.outerHTML)
                     }
                    else{
                        el.insertAdjacentHTML("beforebegin", tag.innerHTML)
                    }
                })
            } 
            if( tag.hasAttribute("mix-after-begin") ){            
                document.querySelectorAll(tag.getAttribute("mix-after-begin")).forEach(el=>{                  
                    if( tag.hasAttribute("mix-url") ){
                        el.insertAdjacentHTML("afterbegin", tag.outerHTML)
                     }
                    else{                    
                        el.insertAdjacentHTML("afterbegin", tag.innerHTML)
                    }
                })
            }  
            if( tag.hasAttribute("mix-before-end") ){            
                document.querySelectorAll(tag.getAttribute("mix-before-end")).forEach(el=>{                  
                    if( tag.hasAttribute("mix-url") ){
                        el.insertAdjacentHTML("beforeend", tag.outerHTML)
                     }
                    else{                    
                        el.insertAdjacentHTML("beforeend", tag.innerHTML)
                    }
                })
            } 
            if( tag.hasAttribute("mix-after-end") ){            
                document.querySelectorAll(tag.getAttribute("mix-after-end")).forEach(el=>{                  
                    if( tag.hasAttribute("mix-url") ){
                        el.insertAdjacentHTML("afterend", tag.outerHTML)
                     }
                    else{
                        el.insertAdjacentHTML("afterend", tag.innerHTML)
                    }
                })
            }

            if( tag.hasAttribute("mix-hide") && ! tag.hasAttribute("mix-url") ){  
                if( tag.getAttribute("mix-hide") !== "" ){
                    const fade = fades.find(v => tag.hasAttribute(`mix-fade-${v}`)) || 0
                    document.querySelectorAll(tag.getAttribute("mix-hide")).forEach(el=>{                  
                        el.setAttribute("mix-hide", "")
                        el.setAttribute(`mix-fade-${fade}`, "")

                    })
                }                          
            }
            if( tag.hasAttribute("mix-show") && ! tag.hasAttribute("mix-url") ){  
                if( tag.getAttribute("mix-show") !== "" ){
                    const fade = fades.find(v => tag.hasAttribute(`mix-fade-${v}`)) || 0
                    document.querySelectorAll(tag.getAttribute("mix-show")).forEach(el=>{                  
                        el.setAttribute("mix-show", "")
                        el.setAttribute(`mix-fade-${fade}`, "")

                    })
                }                          
            }  
            if( tag.hasAttribute("mix-remove") && ! tag.hasAttribute("mix-url") ){  
                if( tag.getAttribute("mix-remove") !== "" ){
                    const fade = fades.find(v => tag.hasAttribute(`mix-fade-${v}`)) || 0
                    document.querySelectorAll(tag.getAttribute("mix-remove")).forEach(el=>{                  
                        el.setAttribute("mix-remove", "")
                        el.setAttribute(`mix-fade-${fade}`, "")
                    })
                }                          
            }
            if( tag.hasAttribute("mix-update") && ! tag.hasAttribute("mix-url")  ){            
                if( tag.getAttribute("mix-update") !== "" ){  
                    const fade = fades.find(v => tag.hasAttribute(`mix-fade-${v}`)) || 0              
                    document.querySelectorAll(tag.getAttribute("mix-update")).forEach(el=>{                  
                        el.setAttribute(`mix-fade-${fade}`, "")
                        if( el.tagName === "INPUT" ){
                            el.value = tag.innerHTML
                        }else{
                            el.innerHTML = tag.innerHTML                         
                        }
                    })
                }                
            }
            if( tag.hasAttribute("mix-replace") && ! tag.hasAttribute("mix-url")  ){   
                if( tag.getAttribute("mix-replace") !== "" ){ 
                    const fade = fades.find(v => tag.hasAttribute(`mix-fade-${v}`)) || 0                
                    document.querySelectorAll(tag.getAttribute("mix-replace")).forEach(el=>{                    
                        el.setAttribute(`mix-fade-${fade}`, "")
                        el.outerHTML = tag.innerHTML
                    })
                }
            }            
            if( tag.hasAttribute("mix-stop-interval") ){
                const el = document.querySelector( tag.getAttribute("mix-stop-interval") )
                clearInterval( el.getAttribute("mix-interval-id") )
                intervals.pop(el.getAttribute("mix-interval-id"))                
            }
            if(tag.hasAttribute("mix-function")){
                const function_name = tag.getAttribute("mix-function").trim()
                window[function_name](tag.innerHTML)
            } 
            if(tag.hasAttribute("mix-script")){
                const data = tag.getAttribute("mix-script").trim()     
                eval(data)
            }                 
            if(tag.hasAttribute("mix-redirect")){
                const redirect_url = tag.getAttribute("mix-redirect").trim()
                window.location.href = redirect_url
            }

        })
        mix_convert()
    }catch(error){ 
        if(DISPLAY_ERRORS){
            console.error("mix_fetch()", error) 
        }
    }
}

// ##############################
function mix_convert(){
    document.querySelectorAll(`[mix-url], [mix-get], [mix-post], [mix-patch], [mix-put], 
                                [mix-delete], [mix-ttl], [mix-remove], [mix-hide], [mix-show], [mix-interval],
                                [mix-stop-interval],
                                [mix-fade-1000],[mix-fade-2000],[mix-fade-3000],[mix-fade-4000],[mix-fade-5000]`).forEach( el => {
        


        // Only for mix-interval
        try{
            if( el.hasAttribute("mix-interval") ){
                if( el.hasAttribute("mix-get") ){
                    const url = el.getAttribute("mix-get")
                    const interval = el.getAttribute("mix-interval")
                    console.log(url)
                    console.log(interval)
                    const interval_id = setInterval(async function(){                    
                        await mix_fetch(url, "GET", form=false, push_to_history=false, el_cover=false, el=false)                        
                    }, interval)
                    el.removeAttribute("mix-interval")
                    el.removeAttribute("mix-get")
                    intervals.push(interval_id)
                    console.log(intervals)
                    el.setAttribute("mix-interval-id", interval_id)
                    return
                }
                throw new Error("mix-interval must be used together with mix-get");
            }
        }catch(error){ if(DISPLAY_ERRORS){ console.log(error) }}
        // End only for mix-interval
        
        // Only for mix-stop-interval
        try{
            if( el.hasAttribute("mix-stop-interval") ){
                el.setAttribute("onclick", "mixhtml(); return false")
                return
            }
        }catch(error){ if(DISPLAY_ERRORS){ console.log(error) }}
        // End only for mix-stop-interval


        try{
            let set_event = true
            let el_event = "onclick"
            if( el.tagName === "FORM" ){ el_event = "onsubmit" }
            if( el.hasAttribute("mix-focus") ){ el_event = "onfocus" }
            if( el.hasAttribute("mix-blur") ){ el_event = "onblur" }
            if( el.hasAttribute("mix-change") ){ el_event = "onchange" }
            if( el.hasAttribute("mix-input") ){ el_event = "oninput" }
            if( el.hasAttribute("mix-url") && ! el.getAttribute("mix-on") ){ el.setAttribute("mix-on","yes") }
            if( el.hasAttribute("mix-url") && ! el.hasAttribute("mix-ttl") ){ el.setAttribute("mix-ttl", "0") }
        
            if ( el.hasAttribute("mix-remove") ){
                set_event = false     
                let fade = fades.find(v => el.hasAttribute(`mix-fade-${v}`)) || 0
                el.classList.add(`mix-fade-out-${fade}`) 
                setTimeout(()=>{ el.remove() }, fade)                            
            }  
            else if ( el.hasAttribute("mix-hide") && ! el.hasAttribute("mix-url") ){
                set_event = false     
                let fade = fades.find(v => el.hasAttribute(`mix-fade-${v}`)) || 0
                el.classList.add(`mix-fade-out-${fade}`) 
                el.removeAttribute(`mix-hide`) 
                setTimeout(()=>{ 
                    el.classList.remove(`mix-fade-out-${fade}`) 
                    el.removeAttribute(`mix-fade-${fade}`) 
                    el.classList.add(`mix-hidden`) 
                }, fade)                            
            }
            else if ( el.hasAttribute("mix-show") && ! el.hasAttribute("mix-url") ){
                set_event = false
                let fade = fades.find(v => el.hasAttribute(`mix-fade-${v}`)) || 0
                el.classList.remove(`mix-hidden`) 
                el.classList.add(`mix-fade-in-${fade}`) 
                // el.removeAttribute(`mix-hide`) 
                setTimeout(()=>{ 
                    el.removeAttribute(`mix-fade-${fade}`) 
                    el.removeAttribute(`mix-show`) 
                    el.classList.remove(`mix-fade-in-${fade}`) 
                    el.classList.remove(`mix-hidden`) 
                }, fade)                            
            }                            
            else if (fades.some(v => el.hasAttribute(`mix-fade-${v}`))){
                const fade = fades.find(v => el.hasAttribute(`mix-fade-${v}`)) || 0
                set_event = false               
                el.classList.add(`mix-fade-in-${fade}`) 
                setTimeout(()=>{ el.classList.remove(`mix-fade-in-${fade}`) }, fade)
                el.removeAttribute(`mix-fade-${fade}`)                               
            }

            if(el.hasAttribute("mix-ttl")){
                const ttl = el.getAttribute("mix-ttl") || 0
                if( ! /^[0-9]\d*$/.test(ttl) ){
                    console.log("mix-ttl must be an integer starting from 1")
                }else{
                    if(el.hasAttribute("mix-url")){
                        if(!el.hasAttribute("mix-ex")){
                            el.setAttribute("mix-ex", el.getAttribute("mix-ttl"))
                        }
                    }else{
                        setTimeout(()=>{ el.remove() }, ttl)
                        el.removeAttribute("mix-ttl")
                    }
                    return
                }                    
            }   

            if(set_event){ el.setAttribute(el_event, "mixhtml(); return false") }        
        }catch(error){ if(DISPLAY_ERRORS){ console.log(error) }}
    })
}
mix_convert()















