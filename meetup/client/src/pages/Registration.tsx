import React from "react";
import Header from "../components/header/Header";
import RegistrationForm from "../components/auth_form/RegistrationForm";

class Registration extends React.Component {
	render() {
		return (
			<main>
				<Header />
				<div className="h-[calc(100vh-4rem)] w-full flex items-center justify-center bg-pink-50">
					<RegistrationForm />
				</div>
			</main>
		);
	}
}

export default Registration;
