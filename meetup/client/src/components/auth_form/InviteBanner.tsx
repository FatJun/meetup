import React from "react";
import { NavLink } from "react-router-dom";
import URLs from "../../urls";

class InviteBanner extends React.Component {
	render() {
		return (
			<div
				className="group flex items-center bg-gradient-to-br from-pink-500 to-red-500 text-white text-sm px-5 py-8 max-w-md w-0 hover:w-full shadow-xl h-2/3
						 rounded-tr-3xl rounded-br-3xl transition-all duration-1000 ease-in-out relative after:absolute after:bg-white after:w-5 after:h-1 after:right-2 after:top-1/2 
						 before:absolute before:bg-white before:w-5 before:h-1 before:right-2 before:top-1/2 before:rotate-45 after:-rotate-45 before:-translate-y-1.5 after:translate-y-1.5 
						 hover:after:opacity-0 hover:before:opacity-0 before:transition-opacity before:duration-300 after:transition-opacity after:duration-300"
			>
				<div className="flex flex-col items-center text-center max-w-md mx-auto opacity-0 group-hover:opacity-100 ease-in-out transition-opacity duration-300">
					<span className="font-bold text-4xl mb-6">Привет, друг!</span>
					<span className="font-mono font-light">У тебя еще нет аккаунта?</span>
					<span className="font-mono font-light mb-6">
						Ты многое теряешь, мы сможем поднять на новый уровень твое
						планирование, давай -
					</span>
					<NavLink
						to={URLs.Registration}
						className="font-mono font-semibold rounded-3xl border py-2 px-8 hover:scale-105 transition-transform"
					>
						Присоединяйся
					</NavLink>
				</div>
			</div>
		);
	}
}

export default InviteBanner;
