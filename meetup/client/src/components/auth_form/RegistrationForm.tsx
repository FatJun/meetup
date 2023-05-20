import React, { ChangeEvent, FormEvent } from "react";
import InputElement from "./InputElement";
import ButtonElement from "./ButtonElement";
import { UserCreate } from "../../types";
import { Navigate } from "react-router-dom";
import URLs from "../../urls";
import API from "../../api/API";

interface RegistrationFormProps {}

interface RegistrationFormState extends UserCreate {
	isLoginIn: boolean;
}

class RegistrationForm extends React.Component<
	RegistrationFormProps,
	RegistrationFormState
> {
	state: RegistrationFormState = {
		first_name: "",
		last_name: "",
		username: "",
		password: "",
		isLoginIn: false,
	};

	handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
		event.preventDefault();
		const isRegistered = await API.createUser(this.state);
		if (isRegistered === false) return;
		const isLoginIn = await API.loginUser(this.state);
		this.setState({ isLoginIn: isLoginIn });
	};
	handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
		const { name, value } = event.target;
		if (name in this.state) {
			const state: RegistrationFormState = {
				[name]: value,
			} as unknown as RegistrationFormState;
			this.setState(state);
		}
	};

	render() {
		return this.state.isLoginIn ? (
			<Navigate to={URLs.PersonalCabinet(this.state.username)} />
		) : (
			<div className="bg-white w-full max-w-md h-2/3 flex flex-col items-center justify-center shadow-xl rounded-3xl">
				<span className="font-bold text-4xl text-pink-600">Регистрация</span>
				<form
					className="flex flex-col w-full items-center px-5 py-8"
					onSubmit={this.handleSubmit}
				>
					<div className="mb-6">
						<InputElement
							name="username"
							label="Telegram Username"
							placeholder="bornworld"
							onChange={this.handleInputChange}
						/>
						<InputElement
							name="last_name"
							label="Фамилия"
							placeholder="Радимир"
							onChange={this.handleInputChange}
						/>
						<InputElement
							name="first_name"
							label="Имя"
							placeholder="Гайцин"
							onChange={this.handleInputChange}
						/>
						<InputElement
							name="password"
							label="Password"
							type="password"
							placeholder="••••••••"
							onChange={this.handleInputChange}
						/>
					</div>
					<ButtonElement value="Зарегистрироваться" />
				</form>
			</div>
		);
	}
}

export default RegistrationForm;
