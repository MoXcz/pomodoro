package.path = package.path .. ';/home/mocos/dev/workspace/github.com/pomodoro/src/lua/config.lua'
local config = require "config"

local function dump(o)
  if type(o) == 'table' then
    local s = '{ '
    for k, v in pairs(o) do
      if type(k) ~= 'number' then k = '"' .. k .. '"' end
      s = s .. '[ ' .. k .. ' = ' .. dump(v) .. ' ],'
    end
    return s .. ' }'
  else
    return tostring(o)
  end
end

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
