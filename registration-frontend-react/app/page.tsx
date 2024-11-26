"use client";
import { useEffect, useState } from "react";
import Foo from "./Foo";

const Home = () => {
	const [data, setData] = useState(null);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const res = await fetch('/api/test');
				const result = await res.json();
				console.log(result);
				setData(result);

			} catch (error) {
				console.error('Error fetching data', error);
			}
		};
		fetchData()
	}, [])

	return (
		<div>
			<h1>Hello This is nextjs foobar</h1>
			<Foo text="Woohooo"></Foo>
			<div>{data ? JSON.stringify(data) : <>Loading...</>}</div>
		</div>
	);
}

export default Home;
