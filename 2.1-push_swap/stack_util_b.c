/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_util_b.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 17:01:53 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/12 17:02:01 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void ft_print_cost_lis(int **cost_lis, int size)
{
    int i;

    i = 0;
    while (i < size)
    {
        ft_printf("LIS mask [%d]: %d\n", i, *cost_lis[i]);
        i++;
    }
}

void ft_debug_print_lis(int *lis, int size)
{
    int i;

    i = 0;
    ft_printf("LIS Cost: ");
    while (i < size)
    {
        ft_printf("%d ", lis[i]);
        i++;
    }
    ft_printf("\n");
}



int ft_calculate_lis(td_list *stack_a, int size)
{    
    int *costs = malloc(sizeof(int) * size);
    if (!costs) 
        return (0);
    ft_init_array_lis(costs, size, 1);

    int i = 0;
    int max_len = 1;
    td_list *curr = stack_a;

    while (curr != NULL)
    {
        td_list *forw = curr->next;
        int j = i + 1; 
        
        while (forw != NULL)
        {
            if (*(int *)forw->content > *(int *)curr->content)
            {
                if (costs[j] < costs[i] + 1)
                    costs[j] = costs[i] + 1;
            }
            if (costs[j] > max_len)
                max_len = costs[j];
                
            forw = forw->next;
            j++;
        }
        curr = curr->next;
        i++;
    }
    ft_debug_print_lis(costs, size);
    free(costs);
    return (max_len);
}

void ft_mark_lis(td_list *stack_a, int *dp, int size, int max_len)
{
    int current_needed = max_len;
    td_list *temp = stack_a;
    int i = 0;
    ft_lstd_last(stack_a);

}

void ft_init_array_lis( int *lis, int size, int value)
{
    int i;

    i = 0;
    while (i < size)
    {
        lis[i] = value;
        i++;
    }
}

int	*ft_find_lis(td_list **stack_a, int size)
{
    int max_index;
    int *lis_mask;
    int *lis_cost;

    if (size == 0) return (0);

    lis_mask = malloc(sizeof(int) * size);
    if (!lis_cost || !lis_mask)
        return (NULL);
    
    ft_init_array_lis(lis_mask, size, 0);
    ft_printf("LIS cost and mask arrays initialized.\n");
    max_index = ft_calculate_lis(*stack_a, size);
    ft_printf("LIS calculated. Max length: %d\n", max_index);
    ft_debug_print_lis(lis_cost, size);
    ft_set_max_lis_mask(*stack_a, lis_cost, &lis_mask, size, max_index);
    ft_print_cost_lis(&lis_mask, size);
    free(lis_mask);

    return (lis_mask);

}
void ft_set_max_lis_mask(td_list *stack_a, int *lis_cost, int **lis_mask, int size, int max_len)
{
    td_list *temp = stack_a;
    int current_needed = max_len;
    int last_val = 2147483647; // Initialize with INT_MAX
    int i = size - 1;

    ft_lstd_last(temp);

    // 2. Backtrack using prev pointers
    while (temp)
    {
        // Check if this node is the correct next step in our LIS chain
        if (lis_cost[i] == current_needed && *(int *)temp->content < last_val)
        {
            last_val = *(int *)temp->content; // Update 'last' for next comparison
            current_needed--;                 // Look for the next smaller length
            *lis_mask[i] = 1;                        // Mark as PART of LIS
        }
        else
        {
            *lis_mask[i] = 0;                        // Mark as NOT part of LIS
        }
        
        temp = temp->prev; // Move backward
        i--;
    }
}

void    ft_push_non_lis(td_list **stack_a, td_list **stack_b, int *lis, int size)
{
    int i;

    i = 0;
    while (i < size)
    {
        if (lis[i] == 0)
        {
            ft_pb(stack_a, stack_b);
        }
        else
        {
            // Keep in stack_a
            ft_ra(stack_a);
        }
        i++;
    }
}