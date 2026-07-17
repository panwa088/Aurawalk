import {Routes,Route} from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import DashboardPage from "../pages/DashboardPage";
import ExplorerPage from "../pages/ExplorerPage";
import ChatPage from "../pages/ChatPage";
import MarketPage from "../pages/MarketPage";
import PetPage from "../pages/PetPage";
import ProfilePage from "../pages/ProfilePage";

import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";

export function AppRouter(){

return(

<Routes>

<Route path="/" element={<LoginPage/>}/>

<Route path="/register" element={<RegisterPage/>}/>

<Route
path="/dashboard"
element={
<MainLayout>
<DashboardPage/>
</MainLayout>
}
/>

<Route
path="/explorer"
element={
<MainLayout>
<ExplorerPage/>
</MainLayout>
}
/>

<Route
path="/chat"
element={
<MainLayout>
<ChatPage/>
</MainLayout>
}
/>

<Route
path="/market"
element={
<MainLayout>
<MarketPage/>
</MainLayout>
}
/>

<Route
path="/pets"
element={
<MainLayout>
<PetPage/>
</MainLayout>
}
/>

<Route
path="/profile"
element={
<MainLayout>
<ProfilePage/>
</MainLayout>
}
/>

</Routes>

)

}