import React from "react";
import {Meet, User} from "../types";
import { connect } from "react-redux";
import { RootDispatch, RootState } from "../redux/store";
import { setCurrentActiveUser } from "../redux/reducers/users/currentUserSlice";
import Header from "../components/header/Header";
import { Navigate } from "react-router-dom";
import { RiAccountBoxFill } from "react-icons/ri";
import URLs from "../urls";
import { FaCalendarPlus } from "react-icons/fa";
import MeetsList from "../components/personal_cabinet/MeetsList";
import CreateMeetPopup from "../components/personal_cabinet/CreateMeetPopup";

interface PersonalCabinetProps {
	user?: User;
	meets?: Meet[];
	authenticated: boolean;
}

interface PersonalCabinetState {
	isLoading?: boolean;
	isCreateMeetPopupOpen: boolean;
}

interface DispatchProps {
	setCurrentActiveUser: () => void;
}

class PersonalCabinet extends React.Component<
	PersonalCabinetProps & DispatchProps,
	PersonalCabinetState
> {
	state: PersonalCabinetState = {
		isLoading: true,
		isCreateMeetPopupOpen: false,
	};

	async componentDidMount(): Promise<void> {
		this.setState({ isLoading: true });
		await this.props.setCurrentActiveUser();
		this.setState({ isLoading: false });
	}

	private openCreateMeetPopup = () => {
		this.setState({ isCreateMeetPopupOpen: true });
	};

	private closeCreateMeetPopup = () => {
		this.setState({ isCreateMeetPopupOpen: false });
	};

	render() {
		if (this.state.isLoading) {
			return <div></div>;
		}
		const { user, authenticated, meets } = this.props;
		return authenticated && user !== undefined ? (
			<div className="bg-pink-50 min-h-screen min-w-screen">
				<Header />
				<div className="w-full max-w-screen-lg mx-auto">
					<div className="flex justify-between items-center w-full bg-white p-2 mt-5 rounded-tr-lg rounded-tl-lg">
						<div className="flex items-center">
							<div className="w-16 h-16 text-pink-700">
								<RiAccountBoxFill className="w-full h-full" />
							</div>
							<div className="text-pink-900 flex flex-col">
								<span className="text-xl font-bold">
									{user.first_name} {user.last_name}
								</span>
								<span className="text-sm font-mono font-light">
									@{user.username}
								</span>
							</div>
						</div>
						<span className="text-pink-900 text-xl uppercase font-bold mr-5">
							Встречи: {meets?.length}
						</span>
					</div>
					<div className="flex flex-col w-full bg-white rounded-br-lg rounded-bl-lg mt-5 p-4">
						{user.registered_in_telegram ? (
							<>
								<button
									onClick={this.openCreateMeetPopup}
									className="group select-none cursor-pointer ml-auto w-fit flex items-center bg-pink-500 text-white py-1 px-4 rounded-2xl mb-5"
								>
									<span className="font-bold mr-2">Создать встречу</span>
									<FaCalendarPlus className="w-4 h-4 group-hover:scale-110 transition-transform" />
								</button>
								<MeetsList />
							</>
						) : (
							<div className="mx-auto mt-5 pb-5 flex flex-col items-center">
								<span className="text-2xl font-bold text-pink-500">
									Для использования функционала встреч зарегистрируйтесь в нашем
								</span>
								<a
									href="https://t.me/meetup_tz_bot"
									className="block text-pink-600 font-mono text-3xl"
								>
									чат боте
								</a>
							</div>
						)}
					</div>
					{user.registered_in_telegram && (
						<CreateMeetPopup
							currentUser={user}
							isOpen={this.state.isCreateMeetPopupOpen}
							close={this.closeCreateMeetPopup}
						/>
					)}
				</div>
			</div>
		) : (
			<Navigate to={URLs.Login} />
		);
	}
}

const mapStateToProps = (state: RootState): PersonalCabinetProps => ({
	user: state.currentUserReducer.user,
	meets: state.currentUserReducer.meets,
	authenticated: state.currentUserReducer.authenticated,
});

const mapDispatchToProps = (dispatch: RootDispatch): DispatchProps => ({
	setCurrentActiveUser: async () => dispatch(setCurrentActiveUser()),
});

export default connect(mapStateToProps, mapDispatchToProps)(PersonalCabinet);
