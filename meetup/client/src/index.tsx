import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import Root from "./pages/Root";
import URLs from "./urls";
import "./index.css";
import Login from "./pages/Login";
import Registration from "./pages/Registration";
import PersonalCabinet from "./pages/PersonalCabinet";

const Router = createBrowserRouter([
	{
		path: URLs.Home,
		element: <Root />,
	},
	{
		path: URLs.Login,
		element: <Login />,
	},
	{
		path: URLs.Registration,
		element: <Registration />,
	},
	{
		path: URLs.PersonalCabinetUrlPattern,
		element: <PersonalCabinet />,
	},
]);

const root_element = document.getElementById("root");
if (root_element !== null) {
	const root = ReactDOM.createRoot(root_element);

	root.render(
		<React.StrictMode>
			<Provider store={store}>
				<RouterProvider router={Router} />
			</Provider>
		</React.StrictMode>
	);
} else {
	throw new Error("Root Element is Null");
}
