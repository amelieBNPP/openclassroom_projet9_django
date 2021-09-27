// get all the stars
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.post-form')

// const handleStarSelected = (size) => {
//   const children = form.children
//   console.log(children)
//   for (let i=0; i < children.lenght; i++){
//     if(i <= size){
//       children[i].classList.add("checked")
//     }else{
//       children[i].classList.add("checked")
//     }
//   }
// }


const handleSelect = (selection) => {
  switch(selection){
    case 'first':{
      one.classList.add("checked")
      two.classList.remove("checked")
      three.classList.remove("checked")
      four.classList.remove("checked")
      five.classList.remove("checked")
      console.log(1)
      // handleStarSelected(1)
      return
    }
    case 'second':{
      one.classList.add("checked")
      two.classList.add("checked")
      three.classList.remove("checked")
      four.classList.remove("checked")
      five.classList.remove("checked")
      console.log(2)
      // handleStarSelected(2)
      return
    }
    case 'third':{
      one.classList.add("checked")
      two.classList.add("checked")
      three.classList.add("checked")
      four.classList.remove("checked")
      five.classList.remove("checked")
      console.log(3)
      // handleStarSelected(3)
      return
    }
    case 'fourth':{
      console.log(4)
      one.classList.add("checked")
      two.classList.add("checked")
      three.classList.add("checked")
      four.classList.add("checked")
      five.classList.remove("checked")
      // handleStarSelected(4)
      return
    }
    case 'fifth':{
      console.log(5)
      one.classList.add("checked")
      two.classList.add("checked")
      three.classList.add("checked")
      four.classList.add("checked")
      five.classList.add("checked")
      // handleStarSelected(5)
      return
    }
  }
}

const arr = [one, two, three, four, five]
arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
  handleSelect(event.target.id)
}))