import React from 'react';
import ghost from "../../assets/ghost2.gif"
import { Box } from '@chakra-ui/react';

const Loader = () => {
  return (
    <>
        <Box width={["300px", "300px"]} height={["300px", "300px"]}>
            <img src={ghost} alt="Loading"  />
        </Box>
    </>
  );
};

export default Loader;
