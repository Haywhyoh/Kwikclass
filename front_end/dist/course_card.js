const template = document.createElement('template');

template.innerHTML = `
<style>
    .my-4 {
        margin-top: 1rem/* 16px */;
        margin-bottom: 1rem/* 16px */;
    }

    .border {
        border-width: 1px;
    }

    .w-60 {
        width: 15rem/* 240px */;
    }

    .border-border_color {
        border-color: rgba(217, 217, 217, 1);
    }

    .text-base {
        font-size: 1rem/* 16px */;
        line-height: 1.5rem/* 24px */;
    }

    .p-3 {
        padding: 0.75rem/* 12px */;
    }

    .px-3 {
        padding-left: 0.75rem/* 12px */;
        padding-right: 0.75rem/* 12px */;
    }

    .grid {
        display: grid;
    }

    .pb-2 {
        padding-bottom: 0.5rem/* 8px */;
    }

    .grid-cols-2 {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .flex {
        display: flex;
    }

    .gap-2 {
        gap: 0.5rem/* 8px */;
    }

    .text-blur {
        color: rgba(26, 25, 25, 0.2);
    }
    
    .pr-2 {
        padding-right: 0.5rem/* 8px */;
    }
    
    
</style>
<div class= "my-4 border  w-60 border-border_color">
                <div><img src="../images/course_img.png" alt=""></div>
                <div class="text-base p-3">UI/Ux design basics road map</div>
                <div class=" px-3 grid pb-2 grid-cols-2">
                    <div class="flex gap-2">
                        <h4>$165</h4>
                        <h4 class="text-blur">$226</h4>
                    </div>
                    <div class="flex ">
                        <p class="pr-2" >4.5</p>
                        <i class="text-orange ri-star-s-fill"></i>
                        <i class="text-orange ri-star-s-fill"></i>
                        <i class="text-orange ri-star-s-fill"></i>
                        <i class="text-orange ri-star-s-fill"></i>
                        <i class="text-orange ri-star-s-fill"></i>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-10  px-3">
                    <div><img src=""> <p class="text-gray-200">James Clifford</p></div>
                    <div><span>123 456</span> enrolled</div>
                </div>
            </div>
`;

class courseCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open'});
    this.shadowRoot.appendChild(template.content.cloneNode(true));
  }
}

window.customElements.define('course-card', courseCard)
