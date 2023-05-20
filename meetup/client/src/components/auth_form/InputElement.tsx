import React, { ChangeEvent } from "react";
interface InputElementProps {
	type?: "text" | "email" | "password" | "datetime-local";
	label: string;
	name: string;
	placeholder?: string;
	required?: boolean;
	onChange?: (event: ChangeEvent<HTMLInputElement>) => void;
}

class InputElement extends React.Component<InputElementProps> {
	static defaultProps = {
		type: "text",
		placeholder: "",
		required: true,
	};
	render() {
		const { type, label, placeholder, name, required, onChange } = this.props;
		return (
			<div className="flex flex-col p-3">
				<label className="text-gray-600 text-xs font-mono">{label}</label>
				<input
					className="outline-none bg-white placeholder:text-pink-300 text-pink-500"
					type={type}
					name={name}
					placeholder={placeholder}
					onChange={onChange}
					required={required}
				/>
			</div>
		);
	}
}

export default InputElement;
