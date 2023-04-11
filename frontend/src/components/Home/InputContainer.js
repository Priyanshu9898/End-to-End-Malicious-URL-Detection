import React, { useState } from 'react'
import { Input, Stack, InputGroup, InputLeftElement , Button, Box, Text} from '@chakra-ui/react';
import {MdOutlineHttp} from "react-icons/md";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { predictURL } from '../../Utils/APIs';
import axios from 'axios';
import './style.css';
import Loader from './Loader';


const InputContainer = () => {

    const toastOptions = {
        position: "bottom-right",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: false,
        draggable: true,
        progress: undefined,
        theme: "dark",
    };
    

    const [url, setUrl] = useState("");
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);


    const handleChange = (e) => {
        setUrl(e.target.value);
    }

    const handleURL = async (e) => {
        e.preventDefault();
        
        if(!url || url.trim().length === 0){
            
            toast.error("Please Enter the URL", toastOptions);
        }

        
        const apiURL = predictURL;
        // console.log(apiURL);
        
        try{
            setLoading(true);
            const response = await axios.post(apiURL, {'url': url.trim()});
            const result = response.data.prediction;
            console.log(`The prediction is ${result}`);
            setPrediction(result);
            setLoading(false);
        }
        catch(err){
            toast.error("Error Predicting the URL, Enter Your URL Again", toastOptions);
        }


    };

  return (
    <>
    
        <Stack direction={['column', 'column']} spacing={10} alignItems={"center"} justifyContent={"space-between"}>
            <InputGroup size='lg' display={"flex"} gap={5}>
                <InputLeftElement
                    pointerEvents='none'
                    children={<MdOutlineHttp color='gray.300' size={"32px"}  />}
                
                />
                <Input className="inp"  type='text' value={url} onChange={handleChange} name="url" id="url"  size="lg" placeholder='Enter Your URL Here...' color="facebook" errorBorderColor='crimson' focusBorderColor='facebook.400'/>
            </InputGroup>
            
            <Button onClick={handleURL} colorScheme='facebook'>Predict</Button>

            {!prediction && loading ? (
                <>
                    <Loader />
                </>
            ) : (
                <>
                {prediction && loading === false ? (
                    <>
                        <Box>
                            <Text fontSize='4xl'>Prediction Result: <span style={{color:prediction === 'benign' ? "green" : "red" }}>{prediction}</span></Text>
                        </Box>
                    </>
                ) : (
                    <></>
                )}
                </>
            )}
            
        </Stack>
        <ToastContainer />
    </>
  )
}

export default InputContainer;