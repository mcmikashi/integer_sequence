import { rest } from 'msw'

// Mock Data

export const fibonnaci_index_6 = {result: 8}

export const fibonnaci_index_10 = {result: 55}



export const handlers = [
  rest.get(`${import.meta.env.VITE_REST_API_URL}sequence/api/fibonacci/6`, (req, res, ctx) => {
    return res(ctx.status(200), ctx.json(fibonnaci_index_6))
  }),
  rest.get(`${import.meta.env.VITE_REST_API_URL}sequence/api/fibonacci/10`, (req, res, ctx) => {
    return res(ctx.status(200), ctx.json(fibonnaci_index_10))
  }),
  rest.get(`${import.meta.env.VITE_REST_API_URL}sequence/api/fibonacci/404`, (req, res, ctx) => {
    return res(ctx.status(404))
  }),
]