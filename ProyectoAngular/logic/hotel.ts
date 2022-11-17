async function GetHotelById() {
    try {
      // 👇️ const response: Response
      const response = await fetch('http://88.17.26.37:5000/hotel', {
        method: 'POST',
        body: JSON.stringify({
          id: '1',
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }
  
      // 👇️ const result: CreateUserResponse
      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;
    } catch (error) {
      if (error instanceof Error) {
        console.log('error message: ', error.message);
        return error.message;
      } else {
        console.log('unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
  }