import React from "react";
import Header from "../components/header/Header";
import InviteBanner from "../components/auth_form/InviteBanner";
import LoginForm from "../components/auth_form/LoginForm";

class Login extends React.Component {
	render() {
		return (
			<div className="min-h-screen min-w-full bg-pink-50">
				<Header />
				<main className="h-[calc(100vh-4rem)] w-full flex items-center justify-center">
					<div className="flex w-full justify-center h-full items-center">
						<LoginForm />
						<InviteBanner />
					</div>
				</main>
			</div>
		);
	}
}

export default Login;
