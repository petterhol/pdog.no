import { test, expect } from '@playwright/test';
import path from 'path';

const filePath = 'file://' + path.resolve(__dirname, 'collapse-icon.html');

test('icon rotates on collapse toggle', async ({ page }) => {
  await page.goto(filePath);
  const icon = page.locator('#collapseIcon');

  // initial state: right arrow
  await expect(icon).toHaveClass(/fa-arrow-right/);

  // open collapse
  await page.click('a[data-toggle="collapse"]');
  await page.waitForSelector('#collapseContent.show');
  await expect(icon).toHaveClass(/fa-arrow-down/);

  // close collapse
  await page.click('a[data-toggle="collapse"]');
  await page.waitForSelector('#collapseContent:not(.show)');
  await expect(icon).toHaveClass(/fa-arrow-right/);
});
