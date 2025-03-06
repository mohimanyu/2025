import axios from "axios";
import { useEffect, useState } from "react";

const useFetchHook = (url: string) => {
    const [data, setData] = useState();
    const [error, setError] = useState("");
    const [loading, setLoading] = useState<boolean>(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                const response = await axios.get(url);
                setData(response.data);
            } catch (error) {
                setError(error);
            } finally {
                setLoading(false);
            }
        };
    }, [url]);
};
