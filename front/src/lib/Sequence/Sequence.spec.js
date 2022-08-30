import "@testing-library/jest-dom";
import { render, fireEvent, screen, waitFor } from "@testing-library/svelte";
import Sequence from "./Sequence.svelte";

test("shows proper UI when rendered", () => {
  render(Sequence);
  const titleValue = screen.getByText("fibonacci sequence");
  expect(titleValue).toBeInTheDocument();
  const inputLabel = screen.getByLabelText("Index (0 min, 1000 max)");
  expect(inputLabel).toBeInTheDocument();
  const inputNumber = screen.getByRole("spinbutton");
  expect(inputNumber).toBeInTheDocument();
  expect(inputNumber.value).toBe("0");
  const incrementButton = screen.getByRole("button", {
    name: "Increment number",
  });
  expect(incrementButton).toBeInTheDocument();
  const decrementButton = screen.getByRole("button", {
    name: "Decrement number",
  });
  expect(decrementButton).toBeInTheDocument();
  const button = screen.getByText("Submit");
  expect(button).toBeInTheDocument();
  const secondTitle = screen.queryByText("Current search");
  expect(secondTitle).toBeNull();
  const tableTitle = screen.queryByText("History search");
  expect(tableTitle).toBeNull();
  const alertServerError = screen.queryByText(
    "The server is not responding correctly."
  );
  expect(alertServerError).toBeNull();
});

test("get curent index and current result", async () => {
  render(Sequence);
  // Change the value of the input number to 10 with the increment button
  const incrementButton = screen.getByRole("button", {
    name: "Increment number",
  });
  for (let index = 0; index < 10; index++) {
    await fireEvent.click(incrementButton);
  }
  // Check the current value of the input number
  const inputNumber = screen.getByRole("spinbutton");
  expect(inputNumber.value).toBe("10");
  // Submit the index
  const button = screen.getByText("Submit");
  await fireEvent.click(button);

  // Check if current value is displayed
  await waitFor(() => screen.getByText("Current search"));
  await waitFor(() => screen.getByText("10"));
  await waitFor(() => screen.getByText("55"));
});

test("get history", async () => {
  render(Sequence);
  // Change the value of the input number to 6 with the increment button
  const incrementButton = screen.getByRole("button", {
    name: "Increment number",
  });
  for (let index = 0; index < 6; index++) {
    await fireEvent.click(incrementButton);
  }
  // check the current value of the input number
  const inputNumber = screen.getByRole("spinbutton");
  expect(inputNumber.value).toBe("6");

  // Submit the index
  const button = screen.getByText("Submit");
  await fireEvent.click(button);

  // Check if current value is displayed
  await waitFor(() => screen.getByText("Current search"));
  await waitFor(() => screen.getByText("6"));
  await waitFor(() => screen.getByText("8"));

  // Change the value of the input number to 10 (6 (current) + 4) with the increment button
  for (let index = 0; index < 4; index++) {
    await fireEvent.click(incrementButton);
  }

  // Check the current value of the input number
  expect(inputNumber.value).toBe("10");
  await fireEvent.click(button);

  // Check if the new current value is displayed
  await waitFor(() => screen.getByText("Current search"));
  await waitFor(() => screen.getByText("10"));
  await waitFor(() => screen.getByText("55"));

  // Check if the history is displayed
  await waitFor(() => screen.getByText("History search"));
  await waitFor(() => screen.getByText("6"));
  await waitFor(() => screen.getByText("8"));
});

test("alert is showed if the server no respond", async () => {
  render(Sequence);
  //ONLY FOR TEST PURPOSE : Submit a request with index 0 this is not set in the handler so it should return an error

  const inputNumber = screen.getByRole("spinbutton");
  expect(inputNumber.value).toBe("0");

  const button = screen.getByText("Submit");
  await fireEvent.click(button);
  await waitFor(() =>
    screen.getByText("The server is not responding correctly.")
  );
});

test("alert is showed if the server return 404", async () => {
  render(Sequence);
  //ONLY FOR TEST PURPOSE : Submit a request with index 404 return an 404 error
  const incrementButton = screen.getByRole("button", {
    name: "Increment number",
  });
  const button = screen.getByText("Submit");
  for (let index = 0; index < 404; index++) {
    await fireEvent.click(incrementButton);
  }

  const inputNumber = screen.getByRole("spinbutton");
  expect(inputNumber.value).toBe("404");

  await fireEvent.click(button);

  await fireEvent.click(button);
  await waitFor(() => screen.getByRole("alert"));
  await waitFor(() =>
    screen.getByText("The server is not responding correctly.")
  );
});
