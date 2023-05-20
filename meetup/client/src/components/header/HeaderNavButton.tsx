import React from "react";
import { IconType } from "react-icons";

interface HeaderNavElementProps {
	Icon: IconType;
	text: string;
	onClick: () => void;
}

class HeaderNavElement extends React.Component<HeaderNavElementProps> {
	render() {
		const { Icon, text, onClick } = this.props;

		return (
			<li className="bg-pink-600 flex items-center py-2 px-4">
				<button onClick={onClick} className="flex items-center space-x-1">
					<Icon className="text-lg" />
					<span>{text}</span>
				</button>
			</li>
		);
	}
}

export default HeaderNavElement;
