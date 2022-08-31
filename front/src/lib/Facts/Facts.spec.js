import "@testing-library/jest-dom";
import { render, screen, waitFor } from "@testing-library/svelte";
import Facts from "./Facts.svelte";
import { server } from "../../../tests/mocks/server";
import { rest } from "msw";

test("shows proper UI when rendered", async () => {
  render(Facts);
  await waitFor(() => screen.getByText("trivia"));
  await waitFor(() => screen.getByText("random trivia facts"));
  await waitFor(() => screen.getByText("math"));
  await waitFor(() => screen.getByText("random math facts"));
  await waitFor(() => screen.getByText("date"));
  await waitFor(() => screen.getByText("random date facts"));
  await waitFor(() => screen.getByText("year"));
  await waitFor(() => screen.getByText("random year facts"));
});

test("shows proper UI when fething api fail", async () => {
  server.use(
    rest.get(`http://numbersapi.com/random/trivia`, (req, res, ctx) => {
      return res(ctx.status(404));
    }),
    rest.get(`http://numbersapi.com/random/math`, (req, res, ctx) => {
      return res(ctx.status(500));
    })
  );
  render(Facts);
  await waitFor(() => screen.getByText("trivia"));
  await waitFor(() =>
    screen.getByText(
      "44 is the number of candles in a box of Hanukkah candles."
    )
  );
  await waitFor(() => screen.getByText("math"));
  await waitFor(() =>
    screen.getByText(
      "44 is a tribonacci number, a happy number, an octahedral number and a palindromic number."
    )
  );
  await waitFor(() => screen.getByText("date"));
  await waitFor(() => screen.getByText("random date facts"));
  await waitFor(() => screen.getByText("year"));
  await waitFor(() => screen.getByText("random year facts"));
});
