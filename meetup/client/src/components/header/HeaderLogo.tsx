import React from "react";
import { NavLink } from "react-router-dom";
import { BsFillHouseHeartFill } from "react-icons/bs";
import URLs from "../../urls";

class HeaderLogo extends React.Component {
	render() {
		return (
			<div className="font-semibold text-2xl text-white">
				<NavLink
					to={URLs.Home}
					className="flex items-center py-2 px-4 space-x-2 bg-pink-600"
				>
					<span>MeetUP</span>
					<BsFillHouseHeartFill className="text-2xl" />
				</NavLink>
			</div>
		);
	}
}

export default HeaderLogo;
