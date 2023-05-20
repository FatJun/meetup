import React from "react";
import Header from "../components/header/Header";

class Root extends React.Component {
	render() {
		return (
			<div className="min-h-screen min-w-full">
				<Header />
				<main className="w-full max-w-screen-lg mx-auto">
					<div className="bg-white w-full h-full">Hello, world!</div>
				</main>
			</div>
		);
	}
}

export default Root;
