import React from "react";
import { MdAccountBox } from "react-icons/md";
import { IoIosExit } from "react-icons/io";
import HeaderNavElement from "./HeaderNavElement";
import URLs from "../../urls";
import { User } from "../../types";
import { connect } from "react-redux";
import { RootDispatch, RootState } from "../../redux/store";
import {
	logoutCurrentUser,
	setCurrentActiveUser,
} from "../../redux/reducers/users/currentUserSlice";
import HeaderNavButton from "./HeaderNavButton";

interface HeaderNavbarProps {
	user?: User;
	authenticated: boolean;
}

interface DispatchProps {
	setCurrentActiveUser: () => void;
	logoutCurrentUser: () => void;
}

class HeaderNavbar extends React.Component<HeaderNavbarProps & DispatchProps> {
	componentDidMount(): void {
		this.props.setCurrentActiveUser();
	}

	render() {
		const { user, authenticated, logoutCurrentUser } = this.props;

		return (
			<nav className="w-auto">
				<ul className="flex space-x-7 font-medium text-white">
					{authenticated ? (
						<>
							<HeaderNavElement
								Icon={MdAccountBox}
								text="Личный кабинет"
								route={URLs.PersonalCabinet(user?.username as string)}
							/>
							<HeaderNavButton
								Icon={IoIosExit}
								text="Выход"
								onClick={logoutCurrentUser}
							/>
						</>
					) : (
						<HeaderNavElement
							Icon={MdAccountBox}
							text="Авторизация"
							route={URLs.Login}
						/>
					)}
				</ul>
			</nav>
		);
	}
}

const mapStateToProps = (state: RootState): HeaderNavbarProps => ({
	user: state.currentUserReducer.user,
	authenticated: state.currentUserReducer.authenticated,
});

const mapDispatchToProps = (dispatch: RootDispatch): DispatchProps => ({
	setCurrentActiveUser: () => dispatch(setCurrentActiveUser()),
	logoutCurrentUser: () => dispatch(logoutCurrentUser()),
});

export default connect(mapStateToProps, mapDispatchToProps)(HeaderNavbar);
