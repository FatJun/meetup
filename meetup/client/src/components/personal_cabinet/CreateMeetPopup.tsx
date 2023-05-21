import React, { ChangeEvent, FormEvent } from "react";
import { AiFillCloseCircle } from "react-icons/ai";
import InputElement from "../auth_form/InputElement";
import ButtonElement from "../auth_form/ButtonElement";
import { Meet, MeetCreate, User } from "../../types";
import API from "../../api/API";
import { RootDispatch } from "../../redux/store";
import { addMeet } from "../../redux/reducers/users/currentUserSlice";
import { connect } from "react-redux";
import moment from "moment-timezone";
import { TZ } from "../../consts";

interface CreateMeetPopupProps {
	currentUser: User;
	isOpen: boolean;
	close: () => void;
}

interface DispatchProps {
	addMeet: (meet: Meet) => void;
}

interface CreateMeetPopupState extends MeetCreate {
	users: User[];
}

class CreateMeetPopup extends React.Component<
	CreateMeetPopupProps & DispatchProps,
	CreateMeetPopupState
> {
	state: CreateMeetPopupState = {
		users: [],
		name: "",
		description: "",
		start_at: new Date(),
		members_usernames: [],
		creator_id: 0,
	};

	async componentDidMount(): Promise<void> {
		const users: User[] = await API.getUsers();
		this.setState({ users: users });
	}
	private handleSubmitForm = async (event: FormEvent<HTMLFormElement>) => {
		event.preventDefault();
		const { name, description, start_at, members_usernames } = this.state;
		const { currentUser } = this.props;
		const start_at_locale = moment(start_at).tz(TZ).toDate();
		if (members_usernames === undefined) return;
		else if (members_usernames.length < 1) return;
		const meet: Meet | undefined = await API.createMeet({
			name: name,
			description: description,
			start_at: start_at_locale,
			members_usernames: members_usernames,
			creator_id: currentUser.id,
		});
		if (meet !== undefined) {
			this.props.addMeet(meet);
			const form = event.target as HTMLFormElement;
			form.reset();
		}
	};

	handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
		const { name, value } = event.target;
		if (name in this.state) {
			const state: CreateMeetPopupState = {
				[name]: value,
			} as unknown as CreateMeetPopupState;
			this.setState(state);
		}
	};

	handleSelectChange = (event: ChangeEvent<HTMLSelectElement>) => {
		const { name, selectedOptions } = event.target;
		const optionsArray = Array.from(selectedOptions);
		if (name !== "members") return;
		this.setState({
			members_usernames: optionsArray.map((option) => option.value),
		});
	};

	render() {
		const { isOpen, close, currentUser } = this.props;
		const isUserValid = (user: User): boolean =>
			user.registered_in_telegram &&
			user.is_active &&
			user.id !== currentUser.id;
		return (
			isOpen && (
				<div className="shadow-xl flex justify-center items-center absolute inset-0 z-50">
					<div className="relative bg-white rounded-xl p-8">
						<div className="absolute right-2 top-2">
							<button onClick={close}>
								<AiFillCloseCircle className="text-red-500 w-5 h-5" />
							</button>
						</div>
						<form className="flex flex-col" onSubmit={this.handleSubmitForm}>
							<InputElement
								label="Название"
								name="name"
								placeholder="Встреча выпускников"
								onChange={this.handleInputChange}
							/>
							<InputElement
								label="Описание"
								name="description"
								placeholder="Бла бла бла.."
								onChange={this.handleInputChange}
							/>
							<InputElement
								type="datetime-local"
								name="start_at"
								label="Начало"
								onChange={this.handleInputChange}
							/>
							<div className="p-3 flex">
								<select
									multiple={true}
									name="members"
									className="outline-none w-full h-24"
									onChange={this.handleSelectChange}
								>
									{this.state.users.map((user: User) => {
										return (
											isUserValid(user) && (
												<option value={user.username} key={user.id}>
													{user.last_name} {user.first_name} (@{user.username})
												</option>
											)
										);
									})}
								</select>
							</div>
							<ButtonElement value="Создать" />
						</form>
					</div>
				</div>
			)
		);
	}
}

const mapDispatchToProps = (dispatch: RootDispatch): DispatchProps => ({
	addMeet: (meet: Meet) => dispatch(addMeet(meet)),
});

export default connect(null, mapDispatchToProps)(CreateMeetPopup);
