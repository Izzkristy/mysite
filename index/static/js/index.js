function contact(event)
{
	var id = event.target
    var para = document.createElement("p")
    var node = document.createTextNode("zhangze0722@gmail.com")
    para.appendChild(node)
    id.parentNode.appendChild(para)
    id.removeEventListener('click', contact, false)
}
document.getElementById("content").addEventListener('click', contact, false);