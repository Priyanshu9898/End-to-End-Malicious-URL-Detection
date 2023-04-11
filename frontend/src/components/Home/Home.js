import React from 'react'
import {Container, Box} from '@chakra-ui/react';
import Header from './Header';
import InputContainer from './InputContainer';

const Home = () => {
  return (
    <Container maxW={"container.xl"} padding={"20px 0px  40px 20px"}>
        <Header />
        <Box marginTop={["60px", "120px"]} paddingRight={"10px"}>
            <InputContainer />
        </Box>
    </Container>
  )
}

export default Home