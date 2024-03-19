import { createSlice,createAsyncThunk } from "@reduxjs/toolkit";
import PropertyAPIService from "./propertyAPIService";

const initialState = {
    properties:[],
    property:{},
    isError:false,
    isLoading:false,
    isSuccess:false,
    message:'',
};


//get all properties
export const getProperties = createAsyncThunk('properties/getAll',async(_,thunkAPI)=>{
    try{
        return await PropertyAPIService.getProperties();
    } catch (error){
        const message = (error.response &&
                        error.response.data && 
                        error.response.data.message) || 
                        error.message || 
                        error.toString();

        return thunkAPI.rejectWithValue(message)
    }
})
export const propertySlice = createSlice({
    name:'property',
    initialState,
    reducers:{
        reset: (state) => initialState
    },
    extraReducers: (builder)=>{
        builder
        .addCase(getProperties.pending, (state)=>{
            state.isLoading = true
        })
        .addCase(getProperties.fulfilled,(state,actions)=>{
            state.isLoading = false;
            state.isSuccess = true;
            state.properties = actions.payload.results;
        })
        .addCase(getProperties.rejected,(state,actions)=>{
            state.isLoading = false;
            state.isError = true;
            state.message = actions.payload;
        })
    },
})

export const {reset} = propertySlice.actions;
export default propertySlice.reducer