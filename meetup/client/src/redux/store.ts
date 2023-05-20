import { configureStore } from "@reduxjs/toolkit";
import currentUserReducer from "./reducers/users/currentUserSlice";

export const store = configureStore({
	reducer: { currentUserReducer },
});

export type RootState = ReturnType<typeof store.getState>;
export type RootDispatch = typeof store.dispatch;
