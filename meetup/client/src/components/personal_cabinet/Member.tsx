import React from "react";
import { RiAccountBoxFill } from "react-icons/ri";
import { User } from "../../types";

interface MemberProps {
	user: User;
}

class Member extends React.Component<MemberProps> {
	render() {
		const { user } = this.props;
		const { first_name, last_name } = user;
		return (
			<li key={user.id}>
				<div className="flex items-center text-sm">
					<RiAccountBoxFill className="text-base" />
					<span className="pl-1">
						{first_name} {last_name}
					</span>
				</div>
			</li>
		);
	}
}

export default Member;
