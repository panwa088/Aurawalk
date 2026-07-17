import { ReactNode } from "react";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";

interface Props{
    children:ReactNode;
}

export default function MainLayout({children}:Props){

    return(

        <div className="layout">

            <Sidebar/>

            <div className="main">

                <Topbar/>

                <div className="content">

                    {children}

                </div>

            </div>

        </div>

    )

}