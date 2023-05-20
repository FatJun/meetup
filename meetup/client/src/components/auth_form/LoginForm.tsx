import React, { ChangeEvent, FormEvent } from "react";
import InputElement from "./InputElement";
import ButtonElement from "./ButtonElement";
import { UserLogin } from "../../types";
import URLs from "../../urls";
import { Navigate } from "react-router-dom";
import API from "../../api/API";

interface LoginFormProps {}
interface LoginFormState extends UserLogin {
	isLoginIn: boolean;
}

class LoginForm extends React.Component<LoginFormProps, LoginFormState> {
	state: LoginFormState = {
		username: "",
		password: "",
		isLoginIn: false,
	};

	handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
		event.preventDefault();
		const isLoginIn = await API.loginUser(this.state);
		this.setState({ isLoginIn: isLoginIn });
	};
	handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
		const { name, value } = event.target;
		if (name in this.state) {
			const state: LoginFormState = {
				[name]: value,
			} as unknown as LoginFormState;
			this.setState(state);
		}
	};

	render() {
		return this.state.isLoginIn ? (
			<Navigate to={URLs.PersonalCabinet(this.state.username)} />
		) : (
			<div className="bg-white w-full max-w-md h-2/3 flex flex-col items-center justify-center shadow-xl rounded-tl-3xl rounded-bl-3xl">
				<span className="font-bold text-4xl text-pink-600">Авторизация</span>
				<form
					className="flex flex-col w-full items-center px-5 py-8"
					onSubmit={this.handleSubmit}
				>
					<InputElement
						name="username"
						label="Username"
						placeholder="bornworld"
						onChange={this.handleInputChange}
					/>
					<InputElement
						name="password"
						label="Password"
						type="password"
						placeholder="••••••••"
						onChange={this.handleInputChange}
					/>
					<ButtonElement value="Войти" />
				</form>
			</div>
		);
	}
}

export default LoginForm;
