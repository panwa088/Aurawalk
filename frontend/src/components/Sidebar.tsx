import { NavLink } from "react-router-dom";

const menus=[

["🏠","Home","/dashboard"],

["🧭","Explorer","/explorer"],

["💬","Chat","/chat"],

["🐲","Pets","/pets"],

["🛒","Market","/market"],

["👤","Profile","/profile"]

]

export default function Sidebar(){

return(

<div className="sidebar">

<h2>AuraWalk</h2>

{

menus.map(item=>(

<NavLink
key={item[2]}
to={item[2]}
className="menu">

<span>{item[0]}</span>

<span>{item[1]}</span>

</NavLink>

))

}

</div>

)

}