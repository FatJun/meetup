import React from "react";

interface ButtonElementProps {
	value: string;
}

class ButtonElement extends React.Component<ButtonElementProps> {
	render() {
		const { value } = this.props;
		return (
			<input
				className="rounded-2xl bg-pink-500 text-white uppercase px-6 py-1 font-bold text-sm cursor-pointer hover:scale-105 transition-transform"
				type="submit"
				value={value}
			/>
		);
	}
}

export default ButtonElement;
