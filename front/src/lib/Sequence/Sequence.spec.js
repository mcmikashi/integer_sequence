// NOTE: jest-dom adds handy assertions to Jest and it is recommended, but not required.
import '@testing-library/jest-dom';
import { render, fireEvent, screen, waitFor } from '@testing-library/svelte';
import Sequence from './Sequence.svelte';

test('shows proper UI when rendered', () => {
  render(Sequence);
  const titleValue = screen.getByText('fibonacci sequence');
  expect(titleValue).toBeInTheDocument();
  const inputInteger = screen.getByLabelText('Index (0 min, 1000 max)');
  expect(inputInteger ).toBeInTheDocument();
  const button = screen.getByText('Submit');
  expect(button).toBeInTheDocument();
});

test('get curent index and current result', async () => {
 render(Sequence);
 const incrementButton = screen.getByRole("button", {name:"Increment number"});
  for (let index = 0; index < 10; index++) {
    await fireEvent.click(incrementButton);
  }
  const inputNumber = screen.getByRole('spinbutton')
  expect(inputNumber.value).toBe('10')
  const button = screen.getByText('Submit');
  await fireEvent.click(button);

  // change the input value 
  await waitFor(() => screen.getByText('Current search'))
  await waitFor(() => screen.getByText('10'))
  await waitFor(() => screen.getByText('55'))
});

test('get curent index and current result', async () => {
  render(Sequence);
  const incrementButton = screen.getByRole("button", {name:"Increment number"});
   for (let index = 0; index < 10; index++) {
     await fireEvent.click(incrementButton);
   }
   const inputNumber = screen.getByRole('spinbutton')
   expect(inputNumber.value).toBe('10')
   const button = screen.getByText('Submit');
   await fireEvent.click(button);
 
   // change the input value 
   await waitFor(() => screen.getByText('Current search'))
   await waitFor(() => screen.getByText('10'))
   await waitFor(() => screen.getByText('55'))
 });
 
 test('get history', async () => {
  render(Sequence);
  const incrementButton = screen.getByRole("button", {name:"Increment number"});
  const inputNumber = screen.getByRole('spinbutton')
  for (let index = 0; index < 6; index++) {
    await fireEvent.click(incrementButton);
  }
  const button = screen.getByText('Submit');
  expect(inputNumber.value).toBe('6')
  await fireEvent.click(button);

  // base current search 
  await waitFor(() => screen.getByText('Current search'))
  await waitFor(() => screen.getByText('6'))
  await waitFor(() => screen.getByText('8'))

   for (let index = 0; index < 4; index++) {
     await fireEvent.click(incrementButton);
   }
   expect(inputNumber.value).toBe('10')
   await fireEvent.click(button);
 
   // new current search
   await waitFor(() => screen.getByText('Current search'))
   await waitFor(() => screen.getByText('10'))
   await waitFor(() => screen.getByText('55'))

   // historic
   await waitFor(() => screen.getByText('History search'))
   await waitFor(() => screen.getByText('6'))
   await waitFor(() => screen.getByText('8'))
 });


 test('alert is showed if the server no respond', async () => {
  render(Sequence);
  const button = screen.getByText('Submit');
  await fireEvent.click(button);
  await waitFor(() => screen.getByText('The server is not responding correctly.'))
 });

 test('alert is showed if the server return 404', async () => {
  render(Sequence);
  const incrementButton = screen.getByRole("button", {name:"Increment number"});
  const button = screen.getByText('Submit');
  for (let index = 0; index < 404; index++) {
    await fireEvent.click(incrementButton);
  }
  await fireEvent.click(button);
  await waitFor(() => screen.getByRole('alert'));
  await waitFor(() => screen.getByText('The server is not responding correctly.'));
 });