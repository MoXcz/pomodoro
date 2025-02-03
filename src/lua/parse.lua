package.path = package.path .. ';/home/mocos/dev/workspace/github.com/pomodoro/src/lua/config.lua'
local config = require "config"

local function t(o)
  for k, v in pairs(o) do
    if type(v) == 'table' then
      t(v)
    else
      print(k .. "=" .. v)
    end
  end
end

print(t(config))
