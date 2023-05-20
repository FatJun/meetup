import React from "react";
import { Meet } from "../../types";
import MeetComponent from "./MeetComponent";
import { connect } from "react-redux";
import { RootDispatch, RootState } from "../../redux/store";
import { getCurrentActiveUserMeets } from "../../redux/reducers/users/currentUserSlice";

interface MeetsListProps {
	meets: Meet[];
}

interface MeetsListState {
	isLoading: boolean;
}

interface DispatchProps {
	getCurrentActiveUserMeets: () => void;
}

class MeetsList extends React.Component<
	MeetsListProps & DispatchProps,
	MeetsListState
> {
	state: MeetsListState = {
		isLoading: true,
	};

	async componentDidMount(): Promise<void> {
		this.setState({ isLoading: true });
		await this.props.getCurrentActiveUserMeets();
		this.setState({ isLoading: false });
	}

	render() {
		if (this.state.isLoading) {
			return <div></div>;
		}
		const { meets } = this.props;

		return meets.length > 0 ? (
			<ul className="grid grid-cols-3 gap-9 max-h-[calc(100vh-18rem)] overflow-y-auto">
				{this.props.meets.map((meet: Meet) => (
					<MeetComponent meet={meet} key={meet.id} />
				))}
			</ul>
		) : (
			<div className="mx-auto mt-5 pb-5">
				<span className="text-2xl font-bold text-pink-500">Встреч нет</span>
			</div>
		);
	}
}

const mapStateToProps = (state: RootState): MeetsListProps => ({
	meets: state.currentUserReducer.meets,
});

const mapDispatchToProps = (dispatch: RootDispatch): DispatchProps => ({
	getCurrentActiveUserMeets: async () => dispatch(getCurrentActiveUserMeets()),
});

export default connect(mapStateToProps, mapDispatchToProps)(MeetsList);
