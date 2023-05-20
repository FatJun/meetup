import React from "react";
import { IconType } from "react-icons";
import { NavLink } from "react-router-dom";

interface HeaderNavElementProps {
	Icon: IconType;
	text: string;
	route: string;
}

class HeaderNavElement extends React.Component<HeaderNavElementProps> {
	render() {
		const { Icon, text, route } = this.props;

		return (
			<li className="bg-pink-600 flex items-center py-2 px-4">
				<NavLink to={route} className="flex items-center space-x-1">
					<Icon className="text-lg" />
					<span>{text}</span>
				</NavLink>
			</li>
		);
	}
}

export default HeaderNavElement;
