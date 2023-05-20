import React from "react";
import { AiFillCalendar } from "react-icons/ai";
import MembersList from "./MembersList";
import { Meet } from "../../types";
import moment from "moment-timezone";
import { TZ } from "../../consts";

interface MeetComponentProps {
	meet: Meet;
}

class MeetComponent extends React.Component<MeetComponentProps> {
	render() {
		const { meet } = this.props;
		const { name, members, start_at, id, description } = meet;

		const start_at_locale = moment(start_at).tz(TZ);

		return (
			<li className="group bg-pink-500 text-pink-50 p-2 rounded-sm self-start">
				<div>
					<div className="flex items-start justify-between">
						<div className="flex flex-col">
							<span className="text-sm font-bold">{name}</span>
							<div className="flex items-center">
								<AiFillCalendar className="text-sm relative bottom-0.5" />
								<span className="text-xs font-mono ml-1">
									{start_at_locale.format("HH:mm / DD.MM.YYYY")}
								</span>
							</div>
						</div>
						<span className="font-bold text-xs">#{id}</span>
					</div>
					<div>
						<span className="text-xs line-clamp-2 group-hover:line-clamp-none text-pink-200">
							{description}
						</span>
					</div>
					{Array.isArray(members) && <MembersList users={members} />}
				</div>
			</li>
		);
	}
}

export default MeetComponent;
