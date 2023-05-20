import React from "react";
import HeaderNavbar from "./HeaderNavBar";
import HeaderLogo from "./HeaderLogo";

class Header extends React.Component {
	render() {
		return (
			<header className="w-full bg-pink-200/50 sticky top-0 z-50 backdrop-blur-sm">
				<div className="max-w-screen-xl flex items-center justify-between mx-auto py-2 px-2">
					<HeaderLogo />
					<HeaderNavbar />
				</div>
			</header>
		);
	}
}

export default Header;
