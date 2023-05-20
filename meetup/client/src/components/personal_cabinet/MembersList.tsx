import React from "react";
import Member from "./Member";
import { User } from "../../types";

interface MembersListProps {
	users: User[];
}

interface MembersListState {
	isMembersVisible: boolean;
}

class MembersList extends React.Component<MembersListProps, MembersListState> {
	state: MembersListState = {
		isMembersVisible: false,
	};

	private showMembersList = () => {
		this.setState({ isMembersVisible: !this.state.isMembersVisible });
	};

	render() {
		const { users } = this.props;
		const { isMembersVisible } = this.state;
		return users.length > 0 ? (
			<div className="flex flex-col">
				<div className="group/members">
					<div className="select-none text-sm font-bold">
						<span>Участники</span>
						<button className="ml-2" onClick={this.showMembersList}>
							[ <span>{isMembersVisible ? "−" : "+"}</span> ]
						</button>
					</div>
					<ul
						className={`h-full max-h-0 transition-all duration-500 ease-in-out overflow-clip space-y-1 mt-1 ${
							isMembersVisible && "max-h-screen"
						}`}
					>
						{users.map((user: User) => (
							<Member user={user} key={user.id} />
						))}
					</ul>
				</div>
			</div>
		) : (
			<></>
		);
	}
}

export default MembersList;
