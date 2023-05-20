import { PayloadAction, createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { Meet, User } from "../../../types";
import API from "../../../api/API";
import { GetCurrentActiveUserPayload } from "../../../api/responses";

interface UserState {
	user?: User;
	meets: Meet[];
	authenticated: boolean;
	loading: "idle" | "pending" | "succeeded" | "failed";
}

const initialState: UserState = {
	meets: [],
	authenticated: false,
	loading: "idle",
};

export const setCurrentActiveUser = createAsyncThunk(
	"user/setCurrentActiveUser",
	async (): Promise<GetCurrentActiveUserPayload> => {
		const response: GetCurrentActiveUserPayload =
			await API.getCurrentActiveUser();
		return response;
	}
);

export const getCurrentActiveUserMeets = createAsyncThunk(
	"user/getCurrentActiveUserMeets",
	async (): Promise<Meet[]> => {
		const response: Meet[] = await API.getCurrentActiveUserMeets();
		return response;
	}
);

export const logoutCurrentUser = createAsyncThunk(
	"user/logoutCurrentUser",
	async (): Promise<boolean> => {
		const response: boolean = await API.logoutCurrentUser();
		return response;
	}
);

export const currentUserSlice = createSlice({
	name: "user",
	initialState,
	reducers: {
		addMeet: (state, action: PayloadAction<Meet>) => {
			state.meets.push(action.payload);
		},
	},
	extraReducers(builder) {
		builder.addCase(setCurrentActiveUser.fulfilled, (state, action) => {
			state.user = action.payload.user;
			state.authenticated = action.payload.authenticated;
		});
		builder.addCase(logoutCurrentUser.fulfilled, (state, action) => {
			if (action.payload === true) state.user = undefined;
			state.authenticated = !action.payload && state.authenticated; // if user not logged out authenticated will set true, but if only authenticated already were true (bad енглиш)
		});
		builder.addCase(getCurrentActiveUserMeets.fulfilled, (state, action) => {
			state.meets = action.payload;
		});
	},
});

export default currentUserSlice.reducer;
export const { addMeet } = currentUserSlice.actions;
